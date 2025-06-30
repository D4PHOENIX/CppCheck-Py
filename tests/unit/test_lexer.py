import pytest
from backend.src.lexer import Lexer
from backend.src.token import Token

def test_lexer_basic():
    code = 'int x = 42;'
    tokens = list(Lexer(code).generate_tokens())
    expected = [
        Token('KEYWORD', 'int', 1, 1),
        Token('ID', 'x', 1, 5),
        Token('OP', '=', 1, 7),
        Token('LITERAL', 42, 1, 9),
        Token('SEP', ';', 1, 11),
    ]
    assert tokens == expected
    
def test_lexer_multiple_lines():
    code = 'int x = 42;\nfloat y = 3.14;'
    tokens = list(Lexer(code).generate_tokens())
    expected = [
        Token('KEYWORD', 'int', 1, 1),
        Token('ID', 'x', 1, 5),
        Token('OP', '=', 1, 7),
        Token('LITERAL', 42, 1, 9),
        Token('SEP', ';', 1, 11),
        Token('NEWLINE', '\n', 1, 12),
        Token('KEYWORD', 'float', 2, 1),
        Token('ID', 'y', 2, 7),
        Token('OP', '=', 2, 9), 
        Token('LITERAL', 3.14, 2, 11),
        Token('SEP', ';', 2, 15),
    ]
    assert tokens == expected
    
def test_lexer_unexpected_character():
    with pytest.raises(SyntaxError):
        list(Lexer('int x = 42 @;').generate_tokens())