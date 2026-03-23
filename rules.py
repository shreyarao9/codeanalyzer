import ast

def check_print_usage(node):
    """Warns if a print function is used, which might be leftover debug code."""
    # In Python 3, 'print' is a function call, so we look for a Call node
    if isinstance(node, ast.Call):
        # We need to ensure the call is a simple name and that name is 'print'
        if isinstance(node.func, ast.Name) and node.func.id == 'print':
            return f"Line {node.lineno}: 'print' used. Is this leftover debug code?"
    return None

def check_function_length(node):
    """Warns if a function is getting too long (over 15 lines/statements)."""
    if isinstance(node, ast.FunctionDef):
        # node.body contains the list of statements inside the function
        if len(node.body) > 15:
            return f"Line {node.lineno}: Function '{node.name}' is {len(node.body)} statements long. Consider breaking it up."
    return None

def check_many_arguments(node):
    """Warns if a function takes too many arguments (more than 5)."""
    if isinstance(node, ast.FunctionDef):
        # node.args.args is the list of arguments the function takes
        num_args = len(node.args.args)
        if num_args > 5:
            return f"Line {node.lineno}: Function '{node.name}' has {num_args} arguments. Consider simplifying."
    return None

# Group the rules together so we can easily loop through them later
ACTIVE_RULES = [
    check_print_usage,
    check_function_length,
    check_many_arguments
]