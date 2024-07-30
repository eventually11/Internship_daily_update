import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'calculator_2')))
from parse_function import parse_expression

class TestParseFunction(unittest.TestCase):

    def test_parse_expression1(self):
        self.assertEqual(parse_expression("9-8*(9/3+5)"), ['9', '-', '8', '*', '(', '9', '/', '3', '+', '5', ')'])
    
    def test_parse_expression2(self):
        self.assertEqual(parse_expression("1+9+8+5+7*(77/11)"), ['1', '+', '9', '+', '8', '+', '5', '+', '7', '*', '(','77', '/', '11', ')'])

    def test_parse_expression3(self):
        self.assertEqual(parse_expression("()123456+-"), ['(', ')', '123456', '+', '-'])

if __name__ == '__main__':
    unittest.main()