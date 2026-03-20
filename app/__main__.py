"""Command-line interface for the inventory reporter."""

from __future__ import annotations

import argparse
from pathlib import Path

from .inventory import format_report, parse_transactions, summarize_inventory


def main(argv: list[str] | None = None) -> int:
    """Run the inventory reporting command-line interface."""
    parser = _build_parser()
    args = parser.parse_args(argv)

    try:
        text = Path(args.input_file).read_text(encoding="utf-8")
        report = format_report(summarize_inventory(parse_transactions(text)))
    except OSError as exc:
        parser.exit(
            status=1,
            message=f"Error: could not read '{args.input_file}': {exc}\n",
        )
    except ValueError as exc:
        parser.exit(status=1, message=f"Error: {exc}\n")

    print(report)
    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Parse inventory transactions and print final stock levels."
    )
    parser.add_argument(
        "input_file",
        help="Path to a UTF-8 text file containing one 'item,delta' transaction per line.",
    )
    return parser


if __name__ == "__main__":
    raise SystemExit(main())
