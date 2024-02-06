from __future__ import annotations

from contextvars import ContextVar
from pathlib import Path
from typing import TYPE_CHECKING

import attr

if TYPE_CHECKING:
    from amigo.agent_handler import AgentHandler
    from amigo.auto_completer import AutoCompleter
    from amigo.code_context import CodeContext
    from amigo.code_file_manager import CodeFileManager
    from amigo.config import Config
    from amigo.conversation import Conversation
    from amigo.cost_tracker import CostTracker
    from amigo.llm_api_handler import LlmApiHandler
    from amigo.sampler.sampler import Sampler
    from amigo.session_stream import SessionStream
    from amigo.vision.vision_manager import VisionManager

SESSION_CONTEXT: ContextVar[SessionContext] = ContextVar("amigo:session_context")


@attr.define()
class SessionContext:
    cwd: Path = attr.field()
    stream: SessionStream = attr.field()
    llm_api_handler: LlmApiHandler = attr.field()
    cost_tracker: CostTracker = attr.field()
    config: Config = attr.field()
    code_context: CodeContext = attr.field()
    code_file_manager: CodeFileManager = attr.field()
    conversation: Conversation = attr.field()
    vision_manager: VisionManager = attr.field()
    agent_handler: AgentHandler = attr.field()
    auto_completer: AutoCompleter = attr.field()
    sampler: Sampler = attr.field()
