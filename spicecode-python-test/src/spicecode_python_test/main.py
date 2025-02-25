

import os

import tree_sitter_python as tspython
import tree_sitter_ruby as tsruby
import tree_sitter_rust as tsrust
from tree_sitter import Language, Parser

def get_language_for_file(file_path):
    """
    Returns the Tree-sitter language object based on the file extension.
    """
    _, ext = os.path.splitext(file_path)
    if ext == ".py":
        return Language(tspython.language())
    elif ext == ".rb":
        return Language(tsruby.language())
    elif ext == ".rs":
        return Language(tsrust.language())
    else:
        raise ValueError(f"Unsupported file extension: {ext}")
    

# aqui pega o path to falando que javascript e melhor no js vc so bota o path aqui tem que fazer essa merda de os.path.join ta maluco
file_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "code-to-analyze", "example.rs")


# vais ler o arquiov
with open(file_path, "r", encoding="utf-8") as file:
    python_code = file.read()


# inicilizai o parser com a linguagem certa
language = get_language_for_file(file_path)
parser = Parser(language)


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


# conta linhas de comentario
def count_comment_lines_from_tree(tree, python_code):

    comment_lines = 0

    # mesma coisa das outras
    for node in tree.root_node.children:
        if node.type == "comment":

            comment_text = python_code[node.start_byte:node.end_byte]
            comment_lines += comment_text.count("\n") + 1  # adidiidcona 1 pra ultima linha
    return comment_lines






line_count = count_lines_from_tree(tree, python_code)
function_count = count_functions_from_tree(tree)
comment_line_count = count_comment_lines_from_tree(tree, python_code)

print(f"The file has {line_count} lines.")
print(f"The file has {function_count} functions.")
print(f"The file has {comment_line_count} comment lines.")