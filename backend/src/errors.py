"""Custom error classes for parsing and syntax checking.

Defines ParserError for reporting syntax errors with optional line, column, and hints.
"""

class ParserError(Exception):
    """
    Exception raised for syntax errors during parsing.

    Attributes:
        message (str): Explanation of the error.
        line (int): Line number where error occurred.
        column (int): Column number where error occurred.
        hint (str): Optional suggestion for fixing the error.
    """


    def __init__(self, message: str, line: int = None, column: int = None, hint: str = None):
        """
        Initialize a ParserError.

        Args:
            message (str): Error message.
            line (int, optional): Line number.
            column (int, optional): Column number.
            hint (str, optional): Suggestion for fixing the error.
        """
        super().__init__(message)
        self.message = message
        self.line = line
        self.column = column
        self.hint = hint

    def __str__(self):
        """
        Return a formatted error message.
        """
        loc = (
            f"Line {self.line}, Column {self.column}: " if self.line is not None else ""
        )
        hint_str = f"Hint: {self.hint}" if self.hint else ""
        return f"{loc}\n{self.message}\n{hint_str}"
