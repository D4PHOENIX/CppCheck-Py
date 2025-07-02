from .ast import Program, Declaration, Assignment, BinaryOp, Literal, Identifier
from .errors import ParserError

class Parser:
    """
    A simple parser for a C++ language.
    """

    def __init__(self, tokens):
        """
        Initialize the parser with a list of tokens.
        Args:
            tokens (list[Token]): The list of tokens to parse.
        """
        self.tokens = tokens
        self.pos = 0

    def current(self):
        """
        Return the current token or None if at the end.
        Returns:
            Token or None: The current token.
        """
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def advance(self):
        """
        Advance to the next token and return the previous one.
        Returns:
            Token or None: The token before advancing.
        """
        tok = self.current()
        self.pos += 1
        return tok

    def parse(self):
        """
        Parse the list of tokens into an abstract syntax tree (AST).
        Returns:
            Program: The root node of the AST representing the program.
        """
        stmts = []
        while self.current():
            stmts.append(self.statement())
        return Program(statements=stmts)

    def statement(self):
        """
        Parse a single statement (declaration, assignment, or expression statement).
        Returns:
            AST node: The parsed statement node.
        Raises:
            ParserError: If the statement is invalid or incomplete.
        """
        tok = self.current()
        # Declaration
        if tok and tok.type == 'KEYWORD' and tok.value == 'int':
            return self.declaration()
        # Assignment
        if tok and tok.type == 'ID':
            nxt = self.tokens[self.pos+1] if self.pos+1 < len(self.tokens) else None
            if nxt and nxt.type == 'OP' and nxt.value == '=':
                return self.assignment()
        # Expression statement
        expr = self.expression()
        sep = self.current()
        if not (sep and sep.type == 'SEP' and sep.value == ';'):
            raise ParserError(f"Expected ';', got {sep}")
        self.advance()
        return expr

    def declaration(self):
        """
        Parse a variable declaration statement (e.g., 'int x = ...;').
        Returns:
            Declaration: The declaration AST node.
        Raises:
            ParserError: If the declaration is invalid.
        """
        self.advance()
        name = self.advance()
        if not (name and name.type == 'ID'):
            raise ParserError(f"Expected identifier, got {name}")
        eq = self.advance()
        if not (eq and eq.type == 'OP' and eq.value == '='):
            raise ParserError(f"Expected '=', got {eq}")
        value = self.assignment()
        sep = self.current()
        if not (sep and sep.type == 'SEP' and sep.value == ';'):
            raise ParserError(f"Expected ';', got {sep}")
        self.advance()
        return Declaration('int', name.value, value)

    def assignment(self):
        """
        Parse an assignment statement (e.g., 'x = ...;').
        Returns:
            Assignment: The assignment AST node.
        Raises:
            ParserError: If the assignment is invalid.
        """
        name = self.advance()
        self.advance()
        value = self.expression()
        sep = self.current()
        if not (sep and sep.type == 'SEP' and sep.value == ';'):
            raise ParserError(f"Expected ';' got {sep}")
        self.advance()
        return Assignment(name.value, value)

    def expression(self):
        """
        Parse an expression, supporting binary operations.
        Returns:
            AST node: The parsed expression node.
        """
        node = self.primary()
        while True:
            tok = self.current()
            if not (tok and tok.type == 'OP'):
                break
            op = tok.value
            self.advance()
            right = self.primary()
            return BinaryOp(op, node, right)

    def primary(self):
        """
        Parse a primary expression (literal, identifier, or parenthesized expression).
        Returns:
            AST node: The parsed primary expression node.
        Raises:
            ParserError: If the token is unexpected or input ends prematurely.
        """
        tok = self.current()
        if not tok:
            raise ParserError("Unexpected end of input.")
        if tok.type == 'Literal':
            self.advance()
            return Literal(tok.value)
        if tok.type == 'ID':
            self.advance()
            return Identifier(tok.value)
        if tok.type == 'SEP' and tok.value == '(': 
            self.advance()
            expr = self.expression()
            sep = self.current()
            if not (sep and sep.type == 'SEP' and sep.value == ')'):
                raise ParserError(f"Expected ')', got {sep}")
            self.advance()
            return expr
        raise ParserError(f"Unexpected token {tok}")
    