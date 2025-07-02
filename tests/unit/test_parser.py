import pytest
from backend.src.lexer import Lexer
from backend.src.parser import Parser
from backend.src.ast import Declaration, Assignment, BinaryOp, Literal, Identifier
from backend.src.errors import ParserError

def parse(code):
    """
    Helper to lex and parse code into an AST Program node.
    """
    tokens = list(Lexer(code).generate_tokens())
    return Parser(tokens).parse()

def test_parser_declaration():
    prog = parse('int a;')
    decl = prog.statements[0]
    assert isinstance(decl, Declaration)
    # Accept both Identifier and string for name
    if isinstance(decl.name, Identifier):
        assert decl.name.name == 'a'
    else:
        assert decl.name == 'a'
    assert decl.value is None

def test_parser_declaration_with_init():
    with pytest.raises(ParserError):
        parse('int a = 100;')

def test_parser_assignment():
    prog = parse('b = a + 2;')
    assign = prog.statements[0]
    assert isinstance(assign, Assignment)
    assert isinstance(assign.name, Identifier)
    assert assign.name.name == 'b'
    assert isinstance(assign.value, BinaryOp)
    assert assign.value.op == '+'

def test_parser_expression():
    prog = parse('x = 1 + 2;')
    assign = prog.statements[0]
    assert isinstance(assign, Assignment)
    assert isinstance(assign.value, BinaryOp)
    assert assign.value.op == '+'

def test_parser_missing_semicolon():
    with pytest.raises(ParserError) as exc:
        parse('int x')
    err = str(exc.value)
    assert 'Expected' in err

def test_parser_unexpected_token():
    with pytest.raises(ParserError):
        parse('int 123;')