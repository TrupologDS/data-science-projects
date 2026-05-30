"""Chat-format helpers for supervised fine-tuning datasets."""

from __future__ import annotations

from collections.abc import Iterable, Mapping

VALID_ROLES = {"system", "user", "assistant"}


def format_qwen_chat(messages: Iterable[Mapping[str, str]]) -> str:
    """Render messages into a compact Qwen/ChatML-style training string."""
    rendered: list[str] = []
    for message in messages:
        role = message.get("role", "")
        content = message.get("content", "").strip()
        if role not in VALID_ROLES:
            raise ValueError(f"Unsupported chat role: {role!r}")
        if not content:
            raise ValueError(f"Empty content for role: {role!r}")
        rendered.append(f"<|im_start|>{role}\n{content}<|im_end|>")
    return "\n".join(rendered)


def alpaca_to_messages(instruction: str, output: str, system_prompt: str, input_text: str = ""):
    """Convert an Alpaca-style row into system/user/assistant messages."""
    user_content = instruction.strip()
    if input_text.strip():
        user_content = f"{user_content}\n\nContext:\n{input_text.strip()}"
    return [
        {"role": "system", "content": system_prompt.strip()},
        {"role": "user", "content": user_content},
        {"role": "assistant", "content": output.strip()},
    ]
