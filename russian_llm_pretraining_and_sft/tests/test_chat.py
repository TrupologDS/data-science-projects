import pytest

from russian_llm_experiment.chat import alpaca_to_messages, format_qwen_chat


def test_format_qwen_chat_renders_roles() -> None:
    messages = [
        {"role": "system", "content": "Be concise."},
        {"role": "user", "content": "Explain LoRA."},
        {"role": "assistant", "content": "LoRA trains low-rank adapter matrices."},
    ]

    rendered = format_qwen_chat(messages)

    assert rendered.count("<|im_start|>") == 3
    assert "<|im_start|>assistant" in rendered
    assert rendered.endswith("<|im_end|>")


def test_format_qwen_chat_rejects_unknown_role() -> None:
    with pytest.raises(ValueError, match="Unsupported chat role"):
        format_qwen_chat([{"role": "tool", "content": "x"}])


def test_alpaca_to_messages_adds_context() -> None:
    messages = alpaca_to_messages("Summarize", "Done", "System", input_text="Context row")

    assert messages[1]["role"] == "user"
    assert "Context:" in messages[1]["content"]
