"""Token class definition for the lexer and parser.

Defines the Token class, representing a lexical token with type, value, line, and column.
"""

class Token:
    """
    Represents a lexical token.

    Attributes:
        type (str): The type of the token (e.g., 'ID', 'LITERAL').
        value (str): The value of the token.
        line (int): The line number where the token appears.
        column (int): The column number where the token appears.
    """
    def __init__(self, type: str, value: str, line: int, column: int):
        """
        Initialize a Token.
        Args:
            type (str): The type of the token.
            value (str): The value of the token.
            line (int): The line number.
            column (int): The column number.
        """
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self) -> str:
        """
        Return a string representation of the Token.
        """
        return f"Token(type={self.type!r}, value={self.value!r}, line={self.line}, column={self.column})"

    def __eq__(self, other) -> bool:
        """
        Compare two Token objects for equality.
        Args:
            other (Token): The other token to compare.
        Returns:
            bool: True if tokens are equal, False otherwise.
        """
        return (
            isinstance(other, Token)
            and self.type == other.type
            and self.value == other.value
            and self.line == other.line
            and self.column == other.column
        )
