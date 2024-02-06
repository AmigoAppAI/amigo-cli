import asyncio
from asyncio import Event
from asyncio.tasks import Task
from pathlib import Path
from typing import List

from amigo.config import Config
from amigo.errors import AmigoError
from amigo.session import Session
from amigo.session_stream import StreamMessageSource


class PythonClient:
    """A client for interacting with Amigo in python."""

    def __init__(
        self,
        cwd: Path = Path.cwd(),
        paths: List[Path] = [],
        exclude_paths: List[Path] = [],
        ignore_paths: List[Path] = [],
        diff: str | None = None,
        pr_diff: str | None = None,
        config: Config = Config(),
    ):
        """
        Initializes the PythonClient with configuration for interacting with Amigo.

        You must call `startup` to begin the client and `shutdown` to end it.

        Parameters:
        - cwd (Path): The current working directory for the client.
        - paths (List[Path]): A list of paths to include in the analysis.
        - exclude_paths (List[Path]): A list of paths to exclude from the analysis.
        - ignore_paths (List[Path]): A list of paths to ignore for the purpose of analysis.
        - diff (str | None): A treeish diff that amigo will be aware of when making changes.
        - pr_diff (str | None): Like diff but it compares to the common ancester.
        - config (Config): Configuration settings for the client.
        """
        self.cwd = cwd.expanduser().resolve()
        self.paths = paths
        self.exclude_paths = exclude_paths
        self.ignore_paths = ignore_paths
        self.diff = diff
        self.pr_diff = pr_diff
        self.config = config

        self._accumulated_message = ""
        self.stopped = Event()
        self._call_amigo_task = None

    async def _call_amigo(self, message: str):
        input_request_message = await self.session.stream.recv("input_request")
        self.session.stream.send(
            message,
            source=StreamMessageSource.CLIENT,
            channel=f"input_request:{input_request_message.id}",
        )
        if message.strip().lower() == "y":
            await self.wait_for_edit_completion()

        temp = self._accumulated_message
        self._accumulated_message = ""
        return temp

    async def call_amigo(self, message: str):
        """Call Amigo with a message and return the response.

        Behaves the same as talking to amigo as an application so you can use commands.
        """
        self._call_amigo_task = asyncio.create_task(self._call_amigo(message))
        try:
            return await self._call_amigo_task
        except asyncio.CancelledError:
            print(self.session.error)
            raise AmigoError("Session failed")

    async def call_amigo_auto_accept(self, message: str) -> str:
        """Call Amigo with a message and then accept the edits."""
        response = await self.call_amigo(message)
        await self.call_amigo("y")
        return response

    async def wait_for_edit_completion(self):
        await self.session.stream.recv(channel="edits_complete")

    async def _accumulate_messages(self):
        async for message in self.session.stream.listen():
            end = "\n"
            if isinstance(message.extra.get("end"), str):
                end = message.extra["end"]
            self._accumulated_message += message.data + end

    async def _listen_for_client_exit(self):
        await self.session.stream.recv("client_exit")
        await self._stop()

    async def startup(self):
        """Starts up the client, establishing a session and beginning to listen for messages and exit signals."""
        self.session = Session(
            self.cwd,
            self.paths,
            self.exclude_paths,
            self.ignore_paths,
            self.diff,
            self.pr_diff,
            self.config,
        )
        self.session.start()
        self.acc_task = asyncio.create_task(self._accumulate_messages())
        self.exit_task: Task[None] = asyncio.create_task(self._listen_for_client_exit())

    async def shutdown(self):
        """Initiates shutdown of the client, ensuring all tasks are cancelled and the session is properly closed.
        Sends the stop signal to the session and returns when client is fully shutdown.
        """
        self.session.stream.send(None, channel="session_exit")
        await self.stopped.wait()

    async def _stop(self):
        self.acc_task.cancel()
        self.exit_task.cancel()
        if self._call_amigo_task:
            self._call_amigo_task.cancel()
        self.stopped.set()

    def get_conversation(self):
        """Returns the current conversation context from the session."""
        return self.session.ctx.conversation

    def get_cost_tracker(self):
        """Returns the cost tracker from the session context."""
        return self.session.ctx.cost_tracker
