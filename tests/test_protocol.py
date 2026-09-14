"""Protocol-level unit tests."""

import json
from pathlib import Path

from lingya_agents_sdk.client import sign_canonical
from lingya_agents_sdk.events import _tool_extension_model, decode_ai_chat_brief_event, decode_tool_extension
from lingya_agents_sdk.models.unknown_ai_chat_brief_event import UnknownAiChatBriefEvent
from lingya_agents_sdk.sse import decode_sse_lines


def test_all_hmac_golden_vectors() -> None:
    fixture = json.loads((Path(__file__).parents[2] / "lingya-agents-openapi/test-vectors/hmac-v1.json").read_text())
    for case in fixture["cases"]:
        assert sign_canonical(case["secret"], case["canonical"]) == case["signature"]


def test_sse_multiline_and_heartbeat() -> None:
    assert list(decode_sse_lines([": heartbeat", 'data: {"a":', "data: 1}", "", "data: done", ""])) == [
        '{"a":\n1}',
        "done",
    ]


def test_unknown_event_preserves_raw_json() -> None:
    raw = '{"type":"future-event","value":42}'
    event = decode_ai_chat_brief_event(raw)
    assert isinstance(event, UnknownAiChatBriefEvent)
    assert event.type == "future-event"
    assert event.raw_json == raw


def test_every_known_tool_extension_has_an_explicit_model() -> None:
    expected = {
        "planApproval": "PlanApprovalExtensionToolExtension",
        "askUserQuestion": "AskUserQuestionExtensionToolExtension",
        "imageGeneration": "ImageGenerationExtensionToolExtension",
        "sqlQuery": "SqlQueryExtensionToolExtension",
        "sqlQueryResult": "SqlQueryResultExtensionToolExtension",
        "sqlChartResult": "SqlChartResultExtensionToolExtension",
        "mathFormula": "MathFormulaExtensionToolExtension",
        "mathResult": "MathResultExtensionToolExtension",
        "jsRunScript": "JsRunScriptExtensionToolExtension",
        "jsRunScriptResult": "JsRunScriptResultExtensionToolExtension",
        "skillResource": "SkillResourceExtensionToolExtension",
        "taskProgress": "TaskProgressExtensionToolExtension",
    }
    assert {category: _tool_extension_model(category).__name__ for category in expected} == expected


def test_unknown_tool_extension_preserves_raw_json() -> None:
    raw = '{"category":"futureTool","value":42}'
    extension = decode_tool_extension(raw)
    assert extension.category == "futureTool"
    assert extension.raw_json == raw
