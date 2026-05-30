"""Small deterministic evaluation helpers for experiment reports."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GenerationCheck:
    prompt: str
    output: str
    min_chars: int = 20
    required_substrings: tuple[str, ...] = ()

    def passed(self) -> bool:
        if len(self.output.strip()) < self.min_chars:
            return False
        lowered = self.output.lower()
        return all(item.lower() in lowered for item in self.required_substrings)


def evaluate_generation_batch(checks: list[GenerationCheck]) -> dict[str, float | int]:
    """Return deterministic pass-rate metrics for qualitative prompt checks."""
    total = len(checks)
    passed = sum(check.passed() for check in checks)
    pass_rate = passed / total if total else 0.0
    return {"total": total, "passed": passed, "pass_rate": pass_rate}


def summarize_lengths(texts: list[str]) -> dict[str, float | int]:
    """Summarize character lengths without pulling in pandas/numpy."""
    if not texts:
        return {"count": 0, "min_chars": 0, "max_chars": 0, "mean_chars": 0.0}
    lengths = [len(text) for text in texts]
    return {
        "count": len(texts),
        "min_chars": min(lengths),
        "max_chars": max(lengths),
        "mean_chars": sum(lengths) / len(lengths),
    }
