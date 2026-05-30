import pytest

from russian_llm_experiment.preprocessing import (
    make_text_chunks,
    normalize_text,
    token_blocks_from_ids,
)


def test_normalize_text_collapses_whitespace_and_quotes() -> None:
    assert normalize_text("  «hello»\n\nworld  ") == '"hello" world'


def test_make_text_chunks_respects_budget() -> None:
    chunks = make_text_chunks(["a" * 5, "b" * 5, "c" * 5], target_chars=11, min_chars=5)

    assert chunks == ["aaaaa bbbbb", "ccccc"]


def test_token_blocks_from_ids_pads_last_block() -> None:
    blocks = token_blocks_from_ids([10, 11, 12], context_length=5, bos_id=1, eos_id=2, pad_id=0)

    assert blocks == [[1, 10, 11, 12, 2]]


def test_token_blocks_requires_valid_context_length() -> None:
    with pytest.raises(ValueError):
        token_blocks_from_ids([1, 2], context_length=2, bos_id=1, eos_id=2, pad_id=0)
