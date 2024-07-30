import re

def parse_expression(expression):
    tokens = re.findall(r'\d+\.?\d*|\+|\-|\*|\/|\(|\)', expression)
    return tokens

def apply_operator(operators, values):
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    if operator == '+':
        values.append(left + right)
    elif operator == '-':
        values.append(left - right)
    elif operator == '*':
        values.append(left * right)
    elif operator == '/':
        values.append(left / right)

def greater_precedence(op1, op2):
    precedences = {'+': 1, '-': 1, '*': 2, '/': 2}
    return precedences[op1] > precedences[op2]

def evaluate(tokens):
    values = []
    operators = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.isdigit() or ('.' in token and token.replace('.', '', 1).isdigit()):
            values.append(float(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()
        elif token in '+-*/':
            while (operators and operators[-1] in '+-*/' and
                   greater_precedence(operators[-1], token)):
                apply_operator(operators, values)
            operators.append(token)
        i += 1

    while operators:
        apply_operator(operators, values)

    return values[0]

def evaluate_expression(expression):
    tokens = parse_expression(expression)
    result = evaluate(tokens)
    return result

# 示例使用
expression = "3 + 5 * (2 - 8)"
result = evaluate_expression(expression)
print(f"Result of '{expression}' is: {result}")
