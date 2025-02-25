from tree_sitter import Parser
import tree_sitter_python as tspython  # This will provide the Python parser

# Initialize the parser
parser = Parser()

# Load the Python language using the `tree-sitter-python` module
parser.language = tspython.language()  # Set the language directly

# Parse the Python file
def parse_code(file_path: str):
    """Parse the given file and return the AST for Python."""
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.read()

    tree = parser.parse(bytes(code, 'utf-8'))
    return tree

# Example analysis functions
def count_lines(tree):
    """Count the number of lines in the code."""
    root_node = tree.root_node
    return root_node.end_byte // root_node.start_byte

def count_functions(tree):
    """Count the number of functions in the AST."""
    root_node = tree.root_node
    function_count = 0

    for node in root_node.children:
        if node.type == 'function_definition':
            function_count += 1

    return function_count

def count_comments(tree):
    """Count the number of comment lines in the AST."""
    root_node = tree.root_node
    comment_count = 0

    for node in root_node.children:
        if node.type == 'comment':
            comment_count += 1

    return comment_count

def analyze_file(file_path: str):
    """Analyze a Python file and print out counts for lines, functions, and comments."""
    tree = parse_code(file_path)
    
    if tree:
        line_count = count_lines(tree)
        function_count = count_functions(tree)
        comment_count = count_comments(tree)

        print(f"Analysis for {file_path}:")
        print(f"  Lines: {line_count}")
        print(f"  Functions: {function_count}")
        print(f"  Comments: {comment_count}")

if __name__ == "__main__":
    analyze_file("code-to-analyze/python_example.py")
