import pytest

from app import format_report, parse_transactions, summarize_inventory


def test_parse_transactions_skips_blank_lines_and_trims_whitespace() -> None:
    text = "  apples, 3\n\n bananas,-1 \n pears,0\n"

    assert parse_transactions(text) == [
        ("apples", 3),
        ("bananas", -1),
        ("pears", 0),
    ]


def test_parse_transactions_rejects_missing_comma() -> None:
    with pytest.raises(ValueError, match="line 1: transaction must be 'item,delta'"):
        parse_transactions("apples 3")


def test_parse_transactions_rejects_empty_item_name() -> None:
    with pytest.raises(ValueError, match="line 1: item name cannot be empty"):
        parse_transactions(",3")


def test_parse_transactions_rejects_non_integer_delta() -> None:
    with pytest.raises(ValueError, match="line 1: delta must be an integer"):
        parse_transactions("apples,three")


def test_summarize_inventory_accumulates_quantities() -> None:
    transactions = [("apples", 3), ("bananas", 2), ("apples", -1)]

    assert summarize_inventory(transactions) == {"apples": 2, "bananas": 2}


def test_summarize_inventory_rejects_negative_totals() -> None:
    with pytest.raises(ValueError, match="inventory for 'apples' cannot become negative"):
        summarize_inventory([("apples", -1)])


def test_format_report_handles_empty_inventory() -> None:
    assert format_report({}) == "No inventory data."


def test_format_report_sorts_items_for_stable_output() -> None:
    inventory = {"bananas": 2, "apples": 5}

    assert format_report(inventory) == "apples: 5\nbananas: 2"
