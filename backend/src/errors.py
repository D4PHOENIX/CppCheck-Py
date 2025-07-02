class ParserError(Exception):
    """
    Exception raised for syntax errors during parsing.

    Attributes:
        message -- explanation of the error
        line    -- line number where error occurred
        column  -- column number where error occurred
        hint    -- optional suggestion for fixing the error
    """
    def __init__(self, message: str, line: int = None, column: int = None, hint: str = None):
        super().__init__(message)
        self.message = message
        self.line = line
        self.column = column
        self.hint = hint

    def __str__(self):
        loc = f"Line {self.line}, Column {self.column}: " if self.line is not None else ""
        hint_str = f" Hint: {self.hint}" if self.hint else ""
        return f"{loc}{self.message}{hint_str}"