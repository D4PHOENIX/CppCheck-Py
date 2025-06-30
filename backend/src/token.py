class Token:
    def __init__(self, type: str, value: str, line: int, column: int):
        self.type = type
        self.value = value
        self.line = line
        self.column = column
        
    def __repr__(self) -> str:
        return f"Token(type={self.type!r}, value={self.value!r}, line={self.line}, column={self.column})"
    
    def __eq__(self, other) -> bool:
        return (
            isinstance(other, Token)
            and self.type == other.type
            and self.value == other.value
            and self.line == other.line
            and self.column == other.column
        )