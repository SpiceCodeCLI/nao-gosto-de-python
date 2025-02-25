

import os

import tree_sitter_python as tspython
from tree_sitter import Language, Parser

PY_LANGUAGE = Language(tspython.language())

parser = Parser(PY_LANGUAGE)


# Specify the path to the Python file you want to parse
file_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "code-to-analyze", "example.py")


# Read the content of the Python file
with open(file_path, "r", encoding="utf-8") as file:
    python_code = file.read()

# Parse the content of the Python file
tree = parser.parse(bytes(python_code, "utf8"))

# Now, you can work with the parsed tree...
def count_lines_from_tree(tree, python_code):
    # Traverse the tree and get the range of the last node
    last_node = tree.root_node
    last_byte = last_node.end_byte

    # Count the number of newlines in the code up to the last byte position
    line_count = python_code[:last_byte].count("\n") + 1  # Add 1 for the last line

    return line_count

# Count the lines using the tree object and the code content
line_count = count_lines_from_tree(tree, python_code)
print(f"The file has {line_count} lines.")