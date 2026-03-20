import runpy
import sys

import pytest

from app.__main__ import main


def test_main_prints_inventory_report(tmp_path, capsys: pytest.CaptureFixture[str]) -> None:
    input_file = tmp_path / "transactions.txt"
    input_file.write_text("apples,3\nbananas,2\napples,-1\n", encoding="utf-8")

    assert main([str(input_file)]) == 0

    captured = capsys.readouterr()
    assert captured.out == "apples: 2\nbananas: 2\n"
    assert captured.err == ""


def test_main_exits_for_missing_file(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exc_info:
        main(["missing.txt"])

    captured = capsys.readouterr()
    assert exc_info.value.code == 1
    assert "Error: could not read 'missing.txt'" in captured.err


def test_main_exits_for_invalid_transaction_file(
    tmp_path, capsys: pytest.CaptureFixture[str]
) -> None:
    input_file = tmp_path / "transactions.txt"
    input_file.write_text("apples,not-a-number\n", encoding="utf-8")

    with pytest.raises(SystemExit) as exc_info:
        main([str(input_file)])

    captured = capsys.readouterr()
    assert exc_info.value.code == 1
    assert "Error: line 1: delta must be an integer" in captured.err


def test_module_entrypoint_runs_main(
    tmp_path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    input_file = tmp_path / "transactions.txt"
    input_file.write_text("pears,4\n", encoding="utf-8")

    monkeypatch.setattr(sys, "argv", ["python", str(input_file)])

    with pytest.raises(SystemExit) as exc_info:
        runpy.run_module("app", run_name="__main__")

    captured = capsys.readouterr()
    assert exc_info.value.code == 0
    assert captured.out == "pears: 4\n"
    assert captured.err == ""
