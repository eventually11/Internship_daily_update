import sys
import os
import unittest

# Add the path to the calculator module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'calculator')))

from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Calculator("2 + 3").evaluate(), 5)

    def test_subtraction(self):
        self.assertEqual(Calculator("5 - 2").evaluate(), 3)

    def test_multiplication(self):
        self.assertEqual(Calculator("3 * 4").evaluate(), 12)

    def test_division(self):
        self.assertEqual(Calculator("8 / 2").evaluate(), 4)

    def test_precedence(self):
        self.assertEqual(Calculator("2 + 3 * 4").evaluate(), 14)

    def test_parentheses(self):
        self.assertEqual(Calculator("(2 + 3) * 4").evaluate(), 20)

if __name__ == "__main__":
    unittest.main()