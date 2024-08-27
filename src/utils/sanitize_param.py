import re


def run(input: str) -> str:
    input = input.strip()

    input = re.sub(r"\s+", "-", input)

    input = re.sub(r"[/.]", "", input)

    input = input.lower()

    return input
