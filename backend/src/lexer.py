import re
from .token import Token

class Lexer:
    # C++ keywords subset
    KEYWORDS = {'int', 'float', 'if', 'else', 'while', 'return', 'for', 'do'}

    def __init__(self, code: str):
        self.code = code
        self.line = 1
        self.column = 1
        self.token_specs = [
            # Literals: numbers or double-quoted strings
            ('LITERAL',  r'(?:\d+(?:\.\d+)?)|"(?:\\.|[^"\\])*"'),
            ('ID',       r'[A-Za-z_][A-Za-z0-9_]*'),
            ('OP',       r'==|!=|<=|>=|[+\-*/=<>]'),
            ('SEP',      r'[;,(){}]'),
            ('NEWLINE',  r'\n'),
            ('SKIP',     r'[ \t]+'),
            ('MISMATCH', r'.'),
        ]
        # Build a single regex with named groups
        self.regex = re.compile(
            '|'.join(f"(?P<{name}>{pattern})" for name, pattern in self.token_specs)
        )

    def generate_tokens(self):
        """Produce a stream of Token(type, value, line, column)."""
        for match_obj in self.regex.finditer(self.code):
            kind      = match_obj.lastgroup
            raw_value = match_obj.group()
            length    = len(raw_value)

            if kind == 'NEWLINE':
                yield Token('NEWLINE', raw_value, self.line, self.column)
                self.line  += 1
                self.column = 1
                continue

            if kind == 'SKIP':
                self.column += length
                continue

            if kind == 'MISMATCH':
                raise SyntaxError(
                    f"Unexpected character {raw_value!r} at line {self.line}, column {self.column}"
                )

            # By default, the token’s value is the raw string
            value = raw_value

            # 1) Reclassify identifiers as keywords
            if kind == 'ID' and value in self.KEYWORDS:
                kind = 'KEYWORD'

            # 2) Convert numeric literals to int/float (leave strings as-is)
            if kind == 'LITERAL' and not (value.startswith('"') and value.endswith('"')):
                if '.' in value:
                    value = float(value)
                else:
                    value = int(value)

            yield Token(kind, value, self.line, self.column)
            # Use the original raw_value length to advance column
            self.column += length
