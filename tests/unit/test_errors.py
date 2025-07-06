import pytest
from backend.src.errors import ParserError

def test_parser_error_with_location_and_hint():
    err = ParserError(
        message="Invalid token", line=2, column=5, hint="Check your operators"
    )
    s = str(err)
    assert "Line 2, Column 5:" in s
    assert "Invalid token" in s
    assert "Check your operators" in s

def test_parser_error_location_only():
    err = ParserError("Oops", line=3, column=1)
    assert str(err) == "Line 3, Column 1: Oops"