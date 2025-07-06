"""Command-line interface for the C++-like syntax checker.

This script checks the syntax of a given C/C++ source file and prints the result.
"""
import sys
import pprint
import argparse
from backend.src.checker import Checker
from backend.src.errors import ParserError
from backend.src.utils import pretty_print_ast

def main():
    """
    Entry point for the command-line syntax checker.

    Parses command-line arguments, reads the source file, checks syntax,
    and prints a human-readable result or error message.
    """
    parser = argparse.ArgumentParser(
        description="C++-like syntax checker. Checks the syntax of a given C/C++ source file."
    )
    parser.add_argument("source_file", nargs="?", help="Path to the C/C++ source file to check.")
    args = parser.parse_args()

    if not args.source_file:
        parser.print_help()
        sys.exit(1)

    filename = args.source_file
    try:
        with open(filename, "r") as f:
            code = f.read()
        program = Checker.check_syntax(code)
        print("✅ Syntax is correct!")
        print("\nAbstract Syntax Tree (AST):")
        print(pretty_print_ast(program))
    except FileNotFoundError:
        print(f"❌ File not found: {filename}")
        sys.exit(1)
    except ParserError as e:
        print("❌ Syntax Error detected!")
        print(f"{e}")
        if hasattr(e, 'hint') and e.hint:
            print(f"Hint: {e.hint}")
        sys.exit(1)

if __name__ == "__main__":
    main()
