# python-ai-assisted-dev-sample

Minimal Python 3.11 application for parsing inventory transactions and producing a text report

## Structure

```text
.
|-- .devcontainer/
|   `-- devcontainer.json
|-- .github/
|   `-- workflows/
|       `-- ci.yml
|-- app/
|   |-- __init__.py
|   |-- __main__.py
|   `-- inventory.py
|-- tests/
|   |-- test_cli.py
|   `-- test_inventory.py
`-- pyproject.toml
```

## Execute the application

```bash
python -m pip install -e .[dev]
python -m app sample-transactions.txt
python -m app sample-transactions.txt --serve --host localhost --port 8000
pytest
```

Then open http://localhost:8000 in your browser. The page refreshes automatically and reflects file changes.

## Test coverage
```bash
python -m pip install -e .[dev]
pytest
```