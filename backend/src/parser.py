from typing import List
from .token import Token
from .ast import Program, Declaration, Assignment, BinaryOp, Literal, Identifier
from .errors import ParserError

class Parser:
    """
    Minimal recursive-descent parser for a tiny C++-like subset.
    Grammar:
        program     → statement* EOF
        statement   → declaration | assignment
        declaration → 'int' ID ';'
        assignment  → ID '=' expression ';'
        expression  → primary (OP primary)*
        primary     → LITERAL | ID
    """

    def __init__(self, tokens: List[Token]):
        """
        Initialize the parser with a list of tokens.
        Args:
            tokens (List[Token]): The list of tokens to parse.
        """
        self.tokens = tokens
        self.pos = 0

    def skip_newlines(self):
        """
        Advance past any NEWLINE tokens.
        """
        while self.current.type == 'NEWLINE':
            self.advance()
            
    @property
    def current(self) -> Token:
        """
        Return the current token, or an EOF token if at the end.
        Returns:
            Token: The current token or EOF token.
        """
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        last = self.tokens[-1]
        return Token('EOF', '', last.line, last.column)

    def advance(self) -> Token:
        """
        Advance to the next token and return the previous one.
        Returns:
            Token: The token before advancing.
        """
        tok = self.current
        self.pos += 1
        return tok

    def expect(self, type_: str, value: str = None) -> Token:
        """
        Expect the current token to match type and (optionally) value, else raise error.
        Args:
            type_ (str): The expected token type.
            value (str, optional): The expected token value.
        Returns:
            Token: The matched token.
        Raises:
            ParserError: If the token does not match.
        """
        tok = self.current
        if tok.type != type_ or (value is not None and tok.value != value):
            desc = f"{type_}{' '+value if value else ''}"
            raise ParserError(
                f"Expected {desc} but got '{tok.value}'",
                tok.line, tok.column
            )
        return self.advance()

    def parse(self) -> Program:
        """
        Parse a program: zero or more statements until EOF.
        Returns:
            Program: The root AST node for the program.
        """
        stmts = []
        while self.current.type != 'EOF':
            self.skip_newlines()
            if self.current.type == 'EOF':
                break
            stmts.append(self.parse_statement())
        return Program(stmts)

    def parse_statement(self):
        """
        Parse a statement: declaration or assignment.
        Returns:
            AST node: Declaration or Assignment.
        Raises:
            ParserError: If the statement is invalid.
        """
        self.skip_newlines()
        if self.current.type == 'KEYWORD' and self.current.value == 'int':
            return self.parse_declaration()
        if self.current.type == 'ID':
            return self.parse_assignment()
        tok = self.current
        raise ParserError(
            f"Unexpected token '{tok.value}' in statement",
            tok.line, tok.column,
            hint="Statements must start with a type keyword or identifier."
        )

    def parse_declaration(self) -> Declaration:
        """
        Parse a declaration: 'int' ID ';'.
        Returns:
            Declaration: The declaration AST node.
        """
        self.advance()  # consume 'int'
        id_tok = self.expect('ID')
        sep = self.current
        if sep.type != 'SEP' or sep.value != ';':
            raise ParserError(
                "Expected ';' after declaration",
                sep.line, sep.column,
                hint="Terminate declarations with a semicolon."
            )
        self.advance()
        return Declaration('int', Identifier(id_tok.value), None)

    def parse_assignment(self) -> Assignment:
        """
        Parse an assignment: ID '=' expression ';'.
        Returns:
            Assignment: The assignment AST node.
        """
        id_tok = self.expect('ID')
        self.expect('OP', '=')
        expr = self.parse_expression()
        sep = self.current
        if sep.type != 'SEP' or sep.value != ';':
            raise ParserError(
                "Expected ';' after assignment",
                sep.line, sep.column,
                hint="Terminate assignments with a semicolon."
            )
        self.advance()
        return Assignment(Identifier(id_tok.value), expr)

    def parse_expression(self):
        """
        Parse an expression: primary (OP primary)* (left-associative, no precedence).
        Returns:
            AST node: The parsed expression node.
        """
        node = self.parse_primary()
        while self.current.type == 'OP':
            op_tok = self.advance()
            right = self.parse_primary()
            node = BinaryOp(op_tok.value, node, right)
        return node

    def parse_primary(self):
        """
        Parse a primary: LITERAL or ID.
        Returns:
            AST node: Literal or Identifier.
        Raises:
            ParserError: If the token is not a valid primary.
        """
        tok = self.current
        if tok.type == 'LITERAL':
            self.advance()
            return Literal(tok.value)
        if tok.type == 'ID':
            self.advance()
            return Identifier(tok.value)
        raise ParserError(
            f"Unexpected token '{tok.value}' in expression",
            tok.line, tok.column,
            hint="Expected a literal or identifier."
        )
