import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'calculator')))
from term_function import term

class TermFunctionTestCase(unittest.TestCase):
    def test_term(self):
        # Test case 1: Multiplication and division
        tokens = "3 * 5 / 2 * 8".replace(" ", "")
        self.assertEqual(term(tokens), 60.0)

        # Test case 2: Only multiplication
        tokens = "2 * 4 * 6".replace(" ", "")
        self.assertEqual(term(tokens), 48.0)

        # Test case 3: Only division
        tokens = "10 / 2 / 5".replace(" ", "")
        self.assertEqual(term(tokens), 1.0)

if __name__ == '__main__':
    unittest.main()