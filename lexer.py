import re

def python_lexer(code):
    patterns = [
        (r'\b(?:if|else|while|for|in|def|return)\b', 'KEYWORD'),
        (r'\b(?:True|False|None)\b', 'LITERAL'),
        (r'\b(?:and|or|not)\b', 'LOGICAL_OP'),
        (r'\b\d+\b', 'NUMBER'),
        (r'\b(?:[a-zA-Z_]\w*)\b', 'IDENTIFIER'),
        (r'[\+\-\*/%=]', 'OPERATOR'),
        (r'\b(?:\(|\)|\[|\]|\{|\})\b', 'PUNCTUATION'),
        (r'\'[^\']*\'|\"[^\"]*\"', 'STRING'),
        (r'#.*$', 'COMMENT')
    ]

    combined_pattern = '|'.join('(?P<{}>{})'.format(name, pattern) for pattern, name in patterns)

    tokens = []
    for match in re.finditer(combined_pattern, code):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        tokens.append((token_type, token_value))

    return tokens

code_example = """
def add_numbers(a, b):
    result = a + b
    return result

print(add_numbers(10, 20))
"""

tokens = python_lexer(code_example)

for token_type, token_value in tokens:
    print(f'{token_type}: {token_value}')
