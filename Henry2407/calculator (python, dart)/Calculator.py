# text based calculator by python (+,-,*,/)
class Calculator:
    def __init__(self, expression):
        self.tokens = expression.replace(" ", "") # remove space in expression
        self.index = 0 # track the current token
     
    def evaluate(self): 
       return self.expression()
    
    def expression(self): # identify the addition and subtraction
        result = self.term() 
        while self.index < len(self.tokens) and self.tokens[self.index] in ('+', '-'):
            if self.tokens[self.index] == '+':
                self.index += 1
                result += self.term()
            elif self.tokens[self.index] == '-':
                self.index += 1
                result -= self.term()
        return result
    
    def term(self): # identify the multiplication and division
        result = self.factor()
        while self.index < len(self.tokens) and self.tokens[self.index] in ('*', '/'):
            if self.tokens[self.index] == '*':
                self.index += 1
                result *= self.factor()
            elif self.tokens[self.index] == '/':
                self.index += 1
                result /= self.factor()
        return result

    def factor(self): # identify the number or expression in parentheses
        if self.tokens[self.index] == '(':
            self.index += 1
            result = self.expression()
            self.index += 1
            return result
        else:
            start = self.index
            while self.index < len(self.tokens) and self.tokens[self.index].isdigit():
                self.index += 1
            return int(self.tokens[start:self.index])
        
if __name__ == "__main__":
    expression = "3 + 5 * ( 2 - 8 )"
    calculator = Calculator(expression)
    result = calculator.evaluate()  # Call the evaluate method
    print(result)  # Print the result