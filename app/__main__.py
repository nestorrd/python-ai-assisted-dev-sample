"""Command-line interface for the inventory reporter."""

from __future__ import annotations

import argparse
from pathlib import Path

from .inventory import (
    format_report,
    parse_transactions,
    summarize_inventory,
)
from .web import serve_inventory


def main(argv: list[str] | None = None) -> int:
    """Run the inventory reporting command-line interface."""
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.serve:
        serve_inventory(Path(args.input_file), host=args.host, port=args.port)
        return 0

    try:
        text = Path(args.input_file).read_text(encoding="utf-8")
        inventory = summarize_inventory(parse_transactions(text))
        report = _format_output(inventory, args.format)
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
    parser.add_argument(
        "--format",
        choices=["text"],
        default="text",
        help="Output format (default: text).",
    )
    parser.add_argument(
        "--serve",
        action="store_true",
        help="Run a local web server that auto-refreshes the report.",
    )
    parser.add_argument(
        "--host",
        default="localhost",
        help="Host for web server mode (default: localhost).",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port for web server mode (default: 8000).",
    )
    return parser


def _format_output(inventory: dict[str, int], output_format: str) -> str:
    return format_report(inventory)


if __name__ == "__main__":
    raise SystemExit(main())
