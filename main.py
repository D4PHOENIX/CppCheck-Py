import sys
from backend.src.checker import Checker
from backend.src.errors import ParserError

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <source_file.cpp>")
        sys.exit(1)
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as f:
            code = f.read()
        program = Checker.check_syntax(code)
        print("Syntax OK! Parsed AST:")
        print(program)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        sys.exit(1)
    except ParserError as e:
        print(f"Syntax Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
