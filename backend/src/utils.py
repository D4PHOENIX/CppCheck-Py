"""Utility functions for pretty-printing AST nodes."""

def pretty_print_ast(node, indent=0):
    """
    Recursively pretty-print an AST node.
    Args:
        node: The AST node (dataclass or list).
        indent: Current indentation level.
    """
    pad = "  " * indent
    if isinstance(node, list):
        if not node:
            return pad + "[]"
        # Add blank lines between top-level statements
        return "\n\n".join(pretty_print_ast(item, indent) for item in node)
    elif hasattr(node, "__dataclass_fields__"):
        fields = []
        # If leaf node (only one field), print in one line
        if len(node.__dataclass_fields__) == 1:
            field = next(iter(node.__dataclass_fields__))
            value = getattr(node, field)
            return f"{pad}{node.__class__.__name__}({field}: {pretty_print_ast(value, 0).strip()})"
        for field in node.__dataclass_fields__:
            value = getattr(node, field)
            fields.append(f"{pad}  {field}: {pretty_print_ast(value, indent + 1).strip()}")
        return f"{pad}{node.__class__.__name__}:\n" + "\n".join(fields)
    else:
        return pad + repr(node)