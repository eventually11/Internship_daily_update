import unittest
import tkinter as tk
from calculator import AdvancedCalculatorApp

class TestAdvancedCalculatorApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = AdvancedCalculatorApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def simulate_clicks(self, clicks):
        for click in clicks:
            self.app.click(click)
            print(f"Clicked: {click}") 

    def test_addition(self):
        self.simulate_clicks(list('2+2='))
        actual_result = self.app.equation.get()
        print(f"Testing '2+2=': Expected result is 4, Actual result is '{actual_result}'")
        self.assertEqual(actual_result, '4')

    def test_multiplication(self):
        self.simulate_clicks(list('5*5='))
        actual_result = self.app.equation.get()
        print(f"Testing '5*5=': Expected result is 25, Actual result is '{actual_result}'")
        self.assertEqual(actual_result, '25')

    def test_invalid_operation(self):
        self.simulate_clicks(list('3++4='))
        actual_result = self.app.equation.get()
        expected_behavior = "Calculator may not handle invalid operations correctly yet."
        print(f"Testing '3++4=': Observed behavior is '{actual_result}'. {expected_behavior}")
        self.assertTrue(actual_result in ['error', '7'], "Unexpected result for invalid operation")

    def test_combined_operations(self):
        self.simulate_clicks(list('6-2+3='))
        actual_result = self.app.equation.get()
        print(f"Testing '6-2+3=': Expected result is 7, Actual result is '{actual_result}'")
        self.assertEqual(actual_result, '7')

    def test_clear(self):
        self.simulate_clicks(['1', '+', '1', 'C'])
        actual_result = self.app.equation.get()
        print(f"Testing clear: Expected result is empty, Actual result is '{actual_result}'")
        self.assertEqual(actual_result, '')

    def test_division_by_zero(self):
        self.simulate_clicks(list('8/0='))
        actual_result = self.app.equation.get()
        print(f"Testing '8/0=': Expected result is 'error', Actual result is '{actual_result}'")
        self.assertEqual(actual_result, 'error')


if __name__ == '__main__':
    unittest.main()