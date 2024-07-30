int calculate() {
  return 6 * 7;
}

class Calculator {
  String expression;
  int index = 0;
  List<String> tokens;

  Calculator(this.expression) : tokens = expression.replaceAll(' ', '').split('');

  double evaluate() {
    return _expression();
  }

  double _expression() {
    double result = _term();
    while (index < tokens.length && (tokens[index] == '+' || tokens[index] == '-')) {
      if (tokens[index] == '+') {
        index++;
        result += _term();
      } else if (tokens[index] == '-') {
        index++;
        result -= _term();
      }
    }
    return result;
  }

  double _term() {
    double result = _factor();
    while (index < tokens.length && (tokens[index] == '*' || tokens[index] == '/')) {
      if (tokens[index] == '*') {
        index++;
        result *= _factor();
      } else if (tokens[index] == '/') {
        index++;
        result /= _factor();
      }
    }
    return result;
  }

  double _factor() {
    if (tokens[index] == '(') {
      index++;
      double result = _expression();
      index++; // Skip ')'
      return result;
    } else {
      int start = index;
      while (index < tokens.length && _isDigit(tokens[index])) {
        index++;
      }
      return double.parse(tokens.sublist(start, index).join(''));
    }
  }

  bool _isDigit(String char) {
    return '0'.compareTo(char) <= 0 && '9'.compareTo(char) >= 0;
  }
}

void main() {
  String expression = "3 + 5 * ( 2 - 8 )";
  Calculator calculator = Calculator(expression);
  double result = calculator.evaluate();
  print("Result: $result");
}