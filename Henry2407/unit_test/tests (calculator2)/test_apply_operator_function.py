import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'calculator_2')))
from apply_operator_function import apply_operator

class TestApplyOperatorFunction(unittest.TestCase):

    def test_apply_operator1(self):
        self.assertEqual(apply_operator(['+'], [1, 2]), [3])
    
    def test_apply_operator2(self):
        self.assertEqual(apply_operator(['-'], [1, 2]), [-1])

    def test_apply_operator3(self):
        self.assertEqual(apply_operator(['*'], [2, 3]), [6])

    def test_apply_operator4(self):
        self.assertEqual(apply_operator(['/'], [6, 3]), [2])

if __name__ == '__main__':
    unittest.main()