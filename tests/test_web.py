from pathlib import Path

from app.web import build_live_report_page, format_html_report


def test_build_live_report_page_renders_inventory_table(tmp_path: Path) -> None:
    input_file = tmp_path / "transactions.txt"
    input_file.write_text("bananas,2\napples,3\n", encoding="utf-8")

    page = build_live_report_page(input_file)

    assert "<meta http-equiv=\"refresh\" content=\"1\">" in page
    assert "<tr><td>apples</td><td>3</td></tr>" in page
    assert "<tr><td>bananas</td><td>2</td></tr>" in page


def test_build_live_report_page_renders_error_for_invalid_data(tmp_path: Path) -> None:
    input_file = tmp_path / "transactions.txt"
    input_file.write_text("apples,not-a-number\n", encoding="utf-8")

    page = build_live_report_page(input_file)

    assert "<meta http-equiv=\"refresh\" content=\"1\">" in page
    assert "<title>Inventory Report Error</title>" in page
    assert "Error: line 1: delta must be an integer" in page

def test_format_html_report_handles_empty_inventory() -> None:
    assert format_html_report({}) == (
        "<!doctype html>"
        "<html lang=\"en\">"
        "<head><meta charset=\"utf-8\"><title>Inventory Report</title></head>"
        "<body><h1>Inventory Report</h1><p>No inventory data.</p></body>"
        "</html>"
    )

def test_format_html_report_sorts_items_and_escapes_names() -> None:
    inventory = {"bananas": 2, "<apples>": 5}

    assert format_html_report(inventory) == (
        "<!doctype html>"
        "<html lang=\"en\">"
        "<head><meta charset=\"utf-8\"><title>Inventory Report</title></head>"
        "<body><h1>Inventory Report</h1>"
        "<table>"
        "<thead><tr><th>Item</th><th>Quantity</th></tr></thead>"
        "<tbody>"
        "<tr><td>&lt;apples&gt;</td><td>5</td></tr>"
        "<tr><td>bananas</td><td>2</td></tr>"
        "</tbody>"
        "</table>"
        "</body>"
        "</html>"
    )
