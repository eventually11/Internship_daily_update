import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'calculator')))
from expression_function import expression

class TestExpressionFunction(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(expression("117 + 5"), 122)
        self.assertEqual(expression("99 + 77 + 30"), 206)

    def test_subtraction(self):
        self.assertEqual(expression("800 - 5"), 795)
        self.assertEqual(expression("100 - 887 - 25"), -812)

    def test_mixed_operations(self):
        self.assertEqual(expression("77 + 15 - 52"), 40)
        self.assertEqual(expression("109 + 205 - 58 + 37"), 293)

    def test_spaces(self):
        self.assertEqual(expression(" 37 + 577 "), 614)
        self.assertEqual(expression(" 108 + 200 - 745 "), -437)

    def test_single_number(self):
        self.assertEqual(expression("42"), 42)
        self.assertEqual(expression("0"), 0)

if __name__ == "__main__":
    unittest.main()