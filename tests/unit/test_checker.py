import pytest
from backend.src.checker import Checker
from backend.src.errors import ParserError

def test_checker_success():
    code = "int x; x = x + 2;"
    program = Checker.check_syntax(code)
    assert hasattr(program, "statements")
    assert len(program.statements) == 2

def test_checker_failure():
    with pytest.raises(ParserError):
        Checker.check_syntax("int x 1;")