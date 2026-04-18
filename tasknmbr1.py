import re

# sample input
text = "This is a int = 10 and a + b = 20"

# define token types
keywords = {"int", "float", "if", "else", "for", "while", "and", "or"}
operators = {"+", "-", "*", "/", "=", "==", "<", ">", "<=", ">="}

# tokenize (split by space and symbols)
tokens = re.findall(r'[A-Za-z_]+|\d+|==|<=|>=|[=+\-*/<>]', text)

# function to detect token type
def get_token_type(token):
    if token in keywords:
        return "Keyword"
    elif token in operators:
        return "Operator"
    elif token.isdigit():
        return "Number"
    elif token.isidentifier():
        return "Identifier"
    else:
        return "Unknown"

# print result
print("Token\t\tType")
print("-----------------------")
for token in tokens:
    print(f"{token}\t\t{get_token_type(token)}")