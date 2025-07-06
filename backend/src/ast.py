"""AST node definitions for the C++-like syntax checker.

Defines dataclasses for Program, Declaration, Assignment, BinaryOp, Literal, and Identifier nodes.
"""
from dataclasses import dataclass

@dataclass
class Program:
    """Represents the root node of the AST, containing a list of statements."""
    statements: list

@dataclass
class Declaration:
    """Represents a variable declaration statement."""
    var_type: str
    name: object
    value: object = None

@dataclass
class Assignment:
    """Represents a variable assignment statement."""
    name: str
    value: object

@dataclass
class BinaryOp:
    """Represents a binary operation (e.g., addition, subtraction)."""
    op: str
    left: object
    right: object

@dataclass
class Literal:
    """Represents a literal value (number or string)."""
    value: object

@dataclass
class Identifier:
    """Represents an identifier (variable name)."""
    name: str