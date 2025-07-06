"""Syntax checker for the C++-like language.

Provides the Checker class for tokenizing and parsing code to produce an AST.
"""
from .errors import ParserError
from .lexer import Lexer
from .parser import Parser

class Checker:
    """
    Syntax checker for the language.

    Provides a static method to check code and return the AST.
    """
    @staticmethod
    def check_syntax(code: str):
        """
        Tokenize and parse the given code string.
        Args:
            code (str): The source code to check.
        Returns:
            Program: The root AST node if syntax is correct.
        Raises:
            ParserError: If a syntax error is encountered.
        """
        tokens = list(Lexer(code).generate_tokens())
        try:
            program = Parser(tokens).parse()
        except Exception as e:
            raise ParserError(str(e))
        return program
