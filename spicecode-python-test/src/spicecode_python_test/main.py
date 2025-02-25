

import os

import tree_sitter_python as tspython
from tree_sitter import Language, Parser

PY_LANGUAGE = Language(tspython.language())

parser = Parser(PY_LANGUAGE)

# aqui pega o path to falando que javascript e melhor no js vc so bota o path aqui tem que fazer essa merda de os.path.join ta maluco
file_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "code-to-analyze", "example.py")


# vais ler o arquiov
with open(file_path, "r", encoding="utf-8") as file:
    python_code = file.read()


# usa o tree sitter pra fazer parse do arquivo
tree = parser.parse(bytes(python_code, "utf8"))


# aqui conta quantas linhas tem
def count_lines_from_tree(tree, python_code):
    # traversa a arvore ate o ultimo node
    last_node = tree.root_node
    last_byte = last_node.end_byte

    line_count = python_code[:last_byte].count("\n") + 1  # adiciona 1 pra ultima linha

    return line_count


# aquji conta quantas funcoes tem
def count_functions_from_tree(tree):

    function_count = 0

    # traversa a arvore e conta as fncoes
    for node in tree.root_node.children:
        if node.type == "function_definition":
            function_count += 1
    return function_count






line_count = count_lines_from_tree(tree, python_code)
function_count = count_functions_from_tree(tree)

print(f"The file has {line_count} lines.")
print(f"The file has {function_count} functions.")