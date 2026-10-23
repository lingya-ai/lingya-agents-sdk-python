"""Presigned upload model tests."""

from lingya_agents_sdk.models.generate_pre_signed_url_input import GeneratePreSignedUrlInput
from lingya_agents_sdk.models.generate_pre_signed_url_output import GeneratePreSignedUrlOutput


def test_presign_input_serializes_size_bytes() -> None:
    payload = GeneratePreSignedUrlInput(
        fileName="agent-sft-overall-strategy.md",
        module="ai-chat-attachments",
        contentMd5="BGN0aTOgnUtqM8UMJesATw==",
        sizeBytes=2048,
    ).to_dict()
    assert payload["sizeBytes"] == 2048


def test_presign_output_restores_upload_protocol() -> None:
    output = GeneratePreSignedUrlOutput.from_dict(
        {
            "support": True,
            "fileUk": "file-key",
            "url": "https://objects.example.com/upload",
            "uploadMethod": "POST_FORM",
            "formFields": {"key": "uploads/agent-sft-overall-strategy.md"},
            "maximumBytes": 4096,
        }
    )
    assert output is not None
    assert output.upload_method == "POST_FORM"
    assert output.form_fields == {"key": "uploads/agent-sft-overall-strategy.md"}
    assert output.maximum_bytes == 4096
