from dataclasses import dataclass

@dataclass
class Program:
    statements: list

@dataclass
class Declaration:
    var_type: str
    name: object
    value: object = None
    
@dataclass
class Assignment:
    name: str
    value: object
    
@dataclass
class BinaryOp:
    op: str
    left: object
    right: object
    
@dataclass
class Literal:
    value: object

@dataclass
class Identifier:
    name:str