"""Tiny check for the Integrated Flow Acceptance sandbox."""

from pathlib import Path


def acceptance_file() -> Path:
    return Path(__file__).with_name("ACCEPTANCE.md")


def main() -> int:
    path = acceptance_file()
    text = path.read_text(encoding="utf-8")
    if "Durable reconstruction" not in text:
        raise SystemExit("ACCEPTANCE.md is missing the reconstruction claim")
    print("ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
