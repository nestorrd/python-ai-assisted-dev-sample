"""Local web server for live inventory reporting."""

from __future__ import annotations

from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from collections.abc import Mapping
from html import escape


from .inventory import parse_transactions, summarize_inventory


def build_live_report_page(input_file: Path) -> str:
    """Build an HTML page from the current inventory file contents."""
    try:
        text = input_file.read_text(encoding="utf-8")
        inventory = summarize_inventory(parse_transactions(text))
        report = format_html_report(inventory)
        return report.replace(
            "<head>",
            "<head><meta http-equiv=\"refresh\" content=\"1\">",
            1,
        )
    except (OSError, ValueError) as exc:
        return (
            "<!doctype html>"
            "<html lang=\"en\">"
            "<head>"
            "<meta charset=\"utf-8\">"
            "<meta http-equiv=\"refresh\" content=\"1\">"
            "<title>Inventory Report Error</title>"
            "</head>"
            "<body>"
            "<h1>Inventory Report</h1>"
            f"<p>Error: {exc}</p>"
            "</body>"
            "</html>"
        )


def serve_inventory(input_file: Path, host: str = "localhost", port: int = 8000) -> None:
    """Serve a live-updating inventory webpage at the given host and port."""

    class InventoryHandler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802
            if self.path not in {"/", "/index.html"}:
                self.send_error(HTTPStatus.NOT_FOUND, "Not Found")
                return

            content = build_live_report_page(input_file).encode("utf-8")
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)

        def log_message(self, format: str, *args: object) -> None:  # noqa: A003
            return

    server = ThreadingHTTPServer((host, port), InventoryHandler)
    print(f"Serving inventory report on http://{host}:{port}")
    try:
        server.serve_forever()
    finally:
        server.server_close()

def format_html_report(inventory: Mapping[str, int]) -> str:
    """Render inventory counts as a basic HTML page."""
    if not inventory:
        body = "<p>No inventory data.</p>"
    else:
        rows = "".join(
            (
                "<tr>"
                f"<td>{escape(item)}</td>"
                f"<td>{quantity}</td>"
                "</tr>"
            )
            for item, quantity in sorted(inventory.items())
        )
        body = (
            "<table>"
            "<thead><tr><th>Item</th><th>Quantity</th></tr></thead>"
            f"<tbody>{rows}</tbody>"
            "</table>"
        )

    return (
        "<!doctype html>"
        "<html lang=\"en\">"
        "<head><meta charset=\"utf-8\"><title>Inventory Report</title></head>"
        f"<body><h1>Inventory Report</h1>{body}</body>"
        "</html>"
    )