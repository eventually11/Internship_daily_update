def term(tokens):  # identify the multiplication and division
    index = 0

    def factor():
        nonlocal index
        start = index
        while index < len(tokens) and tokens[index].isdigit():
            index += 1
        return int(tokens[start:index])

    result = factor()
    while index < len(tokens) and tokens[index] in ('*', '/'):
        if tokens[index] == '*':
            index += 1
            result *= factor()
        elif tokens[index] == '/':
            index += 1
            result /= factor()
    return result

# Test the function
tokens = "3 * 5 / 2 * 8".replace(" ", "")
print(term(tokens))  # Print the result