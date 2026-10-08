"""CLI for TXT, PDF and DOCX summarization."""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
from notes_summariser.documents import extract_text
from notes_summariser.summarize import summarize_text


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize a TXT, PDF or DOCX document with BART")
    parser.add_argument("input", type=Path, help="Path to document")
    parser.add_argument("-o", "--output", type=Path, default=Path("summary_output.txt"))
    args = parser.parse_args()
    try:
        text = extract_text(args.input)
        summary = summarize_text(text)
        args.output.write_text(summary + "\n", encoding="utf-8")
    except (OSError, ValueError, ImportError, RuntimeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(f"Summary saved to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
