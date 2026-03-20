"""Inventory transaction parsing and reporting utilities."""

from __future__ import annotations

from collections.abc import Iterable, Mapping

def parse_transactions(text: str) -> list[tuple[str, int]]:
    """Parse inventory transactions from comma-separated text."""
    transactions: list[tuple[str, int]] = []

    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue

        item, delta = _split_transaction(line, line_number)
        transactions.append((item, delta))

    return transactions


def summarize_inventory(transactions: Iterable[tuple[str, int]]) -> dict[str, int]:
    """Calculate final inventory counts from parsed transactions."""
    inventory: dict[str, int] = {}

    for item, delta in transactions:
        new_total = inventory.get(item, 0) + delta
        if new_total < 0:
            raise ValueError(f"inventory for '{item}' cannot become negative")

        inventory[item] = new_total

    return inventory


def format_report(inventory: Mapping[str, int]) -> str:
    """Render inventory counts as a stable, human-readable report."""
    if not inventory:
        return "No inventory data."

    return "\n".join(
        f"{item}: {quantity}" for item, quantity in sorted(inventory.items())
    )

def _split_transaction(line: str, line_number: int) -> tuple[str, int]:
    parts = [part.strip() for part in line.split(",", maxsplit=1)]
    if len(parts) != 2:
        raise ValueError(f"line {line_number}: transaction must be 'item,delta'")

    item, raw_delta = parts
    if not item:
        raise ValueError(f"line {line_number}: item name cannot be empty")

    try:
        delta = int(raw_delta)
    except ValueError as exc:
        raise ValueError(f"line {line_number}: delta must be an integer") from exc

    return item, delta
