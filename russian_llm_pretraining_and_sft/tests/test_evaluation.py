from russian_llm_experiment.evaluation import GenerationCheck, evaluate_generation_batch


def test_generation_batch_pass_rate() -> None:
    checks = [
        GenerationCheck(prompt="a", output="This answer is long enough.", min_chars=10),
        GenerationCheck(prompt="b", output="short", min_chars=10),
    ]

    metrics = evaluate_generation_batch(checks)

    assert metrics == {"total": 2, "passed": 1, "pass_rate": 0.5}


def test_required_substrings_are_case_insensitive() -> None:
    check = GenerationCheck(
        prompt="Explain",
        output="The response mentions LoRA adapters.",
        required_substrings=("lora", "ADAPTERS"),
    )

    assert check.passed()
