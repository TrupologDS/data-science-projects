"""Text preprocessing and causal-LM packing utilities."""

from __future__ import annotations

import re
import unicodedata


def normalize_text(text: str) -> str:
    """Normalize whitespace and common Unicode variants while preserving content."""
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("«", '"').replace("»", '"')
    text = re.sub(r"[\u2010-\u2015]+", "-", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def make_text_chunks(
    sentences: list[str],
    target_chars: int = 1800,
    min_chars: int = 300,
) -> list[str]:
    """Pack cleaned sentences into character-budget chunks."""
    chunks: list[str] = []
    current: list[str] = []
    current_len = 0

    for sentence in sentences:
        sentence = normalize_text(sentence)
        if not sentence:
            continue
        projected_len = current_len + len(sentence) + (1 if current else 0)
        if current and projected_len > target_chars and current_len >= min_chars:
            chunks.append(" ".join(current))
            current = [sentence]
            current_len = len(sentence)
        else:
            current.append(sentence)
            current_len = projected_len

    if current:
        chunks.append(" ".join(current))
    return chunks


def token_blocks_from_ids(
    token_ids: list[int],
    context_length: int,
    bos_id: int,
    eos_id: int,
    pad_id: int,
) -> list[list[int]]:
    """Create fixed-length causal LM blocks from token ids."""
    if context_length < 3:
        raise ValueError("context_length must leave room for BOS, content, and EOS")
    block_content_len = context_length - 2
    blocks: list[list[int]] = []
    for start in range(0, len(token_ids), block_content_len):
        content = token_ids[start : start + block_content_len]
        block = [bos_id, *content, eos_id]
        if len(block) < context_length:
            block.extend([pad_id] * (context_length - len(block)))
        blocks.append(block)
    return blocks
