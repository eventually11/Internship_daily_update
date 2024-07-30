import re

def parse_expression(expression):
    tokens = re.findall(r'\d+\.?\d*|\+|\-|\*|\/|\(|\)', expression)
    return tokens

print(parse_expression("9-8*(9/3+5)")) 