import webbrowser
from typing import List

from typing_extensions import override

from amigo.command.command import Command, CommandArgument
from amigo.session_context import SESSION_CONTEXT
from amigo.transcripts import Transcript, get_transcript_logs
from amigo.utils import create_viewer


class ViewerCommand(Command, command_name="viewer"):
    @override
    async def apply(self, *args: str) -> None:
        session_context = SESSION_CONTEXT.get()
        conversation = session_context.conversation

        logs = get_transcript_logs()

        viewer_path = create_viewer(
            [Transcript(id="Current", messages=conversation.literal_messages)] + logs
        )
        webbrowser.open(f"file://{viewer_path.resolve()}")

    @override
    @classmethod
    def arguments(cls) -> List[CommandArgument]:
        return []

    @override
    @classmethod
    def argument_autocompletions(
        cls, arguments: list[str], argument_position: int
    ) -> list[str]:
        return []

    @override
    @classmethod
    def help_message(cls) -> str:
        return "Open a webpage showing the conversation so far."
