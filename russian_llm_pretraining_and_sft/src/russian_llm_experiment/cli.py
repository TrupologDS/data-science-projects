"""Minimal CLI for deterministic report checks."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from russian_llm_experiment.evaluation import GenerationCheck, evaluate_generation_batch


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate saved prompt generation checks.")
    parser.add_argument("checks_json", type=Path)
    args = parser.parse_args()

    rows = json.loads(args.checks_json.read_text(encoding="utf-8"))
    checks = [GenerationCheck(**row) for row in rows]
    print(json.dumps(evaluate_generation_batch(checks), indent=2))


if __name__ == "__main__":
    main()
