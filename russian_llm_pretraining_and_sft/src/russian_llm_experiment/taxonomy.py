"""Failure categories used during manual generation review."""

ERROR_TAXONOMY = {
    "language_mismatch": "The answer switches away from the requested language.",
    "instruction_miss": "The answer does not address the user instruction.",
    "format_miss": "The answer ignores an expected structure such as bullets or steps.",
    "unsupported_claim": "The answer states a factual claim without support in the prompt/context.",
    "degeneration": "The answer repeats, collapses, or becomes incoherent.",
}
