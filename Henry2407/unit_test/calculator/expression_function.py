def expression(expression_str):  # identify the addition and subtraction
    tokens = expression_str.replace(" ", "")  # remove space in expression
    index = 0

    def number():
        nonlocal index
        start = index
        while index < len(tokens) and tokens[index].isdigit():
            index += 1
        return int(tokens[start:index])

    result = number()  # get the first number
    while index < len(tokens) and tokens[index] in ('+', '-'):
        if tokens[index] == '+':
            index += 1
            result += number()
        elif tokens[index] == '-':
            index += 1
            result -= number()
    return result

# Test the function
expression_str = "3 + 5 - 2 + 8"
print(expression(expression_str))  # Print the result