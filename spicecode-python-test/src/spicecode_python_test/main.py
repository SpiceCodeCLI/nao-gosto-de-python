
import tree_sitter
from tree_sitter import Language


# load all aprsers manually maybe we can automate this in theh tfurure
PYTHON_LANGUAGE = Language('tree-sitter-python.so', 'python')
JAVASCRIPT_LANGUAGE = Language('tree-sitter-javascript.so', 'javascript')
C_LANGUAGE = Language('tree-sitter-c.so', 'c')
RUBY_LANGUAGE = Language('tree-sitter-ruby.so', 'ruby')
LUA_LANGUAGE = Language('tree-sitter-lua.so', 'lua')
RUST_LANGUAGE = Language('tree-sitter-rust.so', 'rust')


# mapping file extensions to langaguesu
LANGUAGES = {
    '.py': PYTHON_LANGUAGE,
    '.js': JAVASCRIPT_LANGUAGE,
    '.c': C_LANGUAGE,
    '.rb': RUBY_LANGUAGE,
    '.lua': LUA_LANGUAGE,
    '.rs': RUST_LANGUAGE,
}


def parse_code(file_path: str):
    """Parse the given file and return the AST for the corresponding language."""
    # select the parser based on fil extension
    ext = file_path.split('.')[-1]
    language = LANGUAGES.get(f'.{ext}')
    
    if not language:
        print(f"Unsupported language for file {file_path}")
        return None

    # read code from file
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.read()

    # start the parser for that langagueu
    parser = tree_sitter.Parser()
    parser.set_language(language)

    # parse the code into AST
    tree = parser.parse(bytes(code, 'utf-8'))

    return tree


# this will count the total of lines
def count_lines(tree):
    """Count the number of lines in the code."""
    root_node = tree.root_node
    return root_node.end_byte // root_node.start_byte

# this will count al lthe functions
def count_functions(tree):
    """Count the number of functions in the AST."""
    root_node = tree.root_node
    function_count = 0

    # traverse the tree and counting functions defiititons
    for node in root_node.children:
        if node.type == 'function_definition':  # this is based on the langague
            function_count += 1

    return function_count

# this will count comment lines
def count_comments(tree):
    """Count the number of comment lines in the AST."""
    root_node = tree.root_node
    comment_count = 0

    # traverse the tree and counting comment nodes
    for node in root_node.children:
        if node.type == 'comment':
            comment_count += 1

    return comment_count


# THIS IS LIKE THE MAIN FUNCTION !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def analyze_file(file_path: str):
    """Analyze a file and print out counts for lines, functions, and comments."""
    tree = parse_code(file_path)
    
    if tree:
        line_count = count_lines(tree)
        function_count = count_functions(tree)
        comment_count = count_comments(tree)

        print(f"Analysis for {file_path}:")
        print(f"  Lines: {line_count}")
        print(f"  Functions: {function_count}")
        print(f"  Comments: {comment_count}")

# PUT THE FILE TO BE ANALUZYED HERE
if __name__ == "__main__":
    analyze_file("code-to-analyze/python_example.py")
