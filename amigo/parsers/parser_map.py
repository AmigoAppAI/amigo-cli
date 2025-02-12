from amigo.parsers.block_parser import BlockParser
from amigo.parsers.json_parser import JsonParser
from amigo.parsers.parser import Parser
from amigo.parsers.replacement_parser import ReplacementParser
from amigo.parsers.unified_diff_parser import UnifiedDiffParser

parser_map: dict[str, Parser] = {
    "block": BlockParser(),
    "replacement": ReplacementParser(),
    "unified-diff": UnifiedDiffParser(),
    # JsonParser is experimental and has no streaming or tests and seems worse than other formats
    # Don't use it! But if you need to, make sure to set to a model that can use the JSON response_format
    "json": JsonParser(),
}
