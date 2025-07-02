from .lexer import Lexer
from .parser import Parser
from .errors import ParserError
class Checker:
    """
    Syntax checker for the language. Provides a method to check code and return the AST.
    """
    @staticmethod
    def check_syntax(code: str):
        """
        Tokenize and parse the given code string.
        Returns a Program AST if successful, or raises ParserError.
        """
        tokens = list(Lexer(code).generate_tokens())
        try:
            program = Parser(tokens).parse()
        except Exception as e:
            raise ParserError(str(e))
        return program
