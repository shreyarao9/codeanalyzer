import ast
from rules import ACTIVE_RULES

def analyze_code(code_string):
    """Parses code into an AST and prints the type of each node."""
    try:
        # 1. Parse the source code into a syntax tree
        tree = ast.parse(code_string)
        warnings = []
        
        # 2. Walk through the nodes
        for node in ast.walk(tree):
            # type(node).__name__ gives us the clean class name (e.g., 'FunctionDef')
            # instead of the full object representation (e.g., <_ast.FunctionDef object at...>)
            # print(type(node).__name__)
            # Pass the node to every active rule
            for rule in ACTIVE_RULES:
                warning = rule(node)
                # If the rule returned a message, save it
                if warning:
                    warnings.append(warning)
            
        if not warnings:
            return "Analysis complete: Code looks clean!"
            
        return "\n".join(warnings)

    except SyntaxError as e:
        # ast.parse will fail if the code we feed it isn't valid Python!
        return f"\nSyntax Error in the analyzed file: {e}"
    except Exception as e:
        return f"\nAn unexpected error occurred: {e}"