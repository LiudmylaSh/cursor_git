#1. Create tests for class Calculator (functions_to_test.py)
#    a. Using unittest lib
#    b. Using pytest lib
import unittest
from functions_to_test import Calculator


class TestFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(0, 1), 1)
        self.assertEqual(Calculator.add(1, 10), 11)
        self.assertEqual(Calculator.add(0.3, 0.2), 0.5)
        self.assertEqual(Calculator.add("13", "13"), "1313")

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(4, 2), 2)
        self.assertEqual(Calculator.subtract(10, 0), 10)
        self.assertEqual(Calculator.subtract(7, -3), 10)
        self.assertEqual(Calculator.subtract(0.4, 0.2), 0.2)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(0, 0), 0)
        self.assertEqual(Calculator.multiply(1, -2), -2)
        self.assertEqual(Calculator.multiply(-10, -10), 100)
        self.assertEqual(Calculator.multiply("7", 3), "777")

    def test_divide(self):
        self.assertEqual(Calculator.divide(10, 10), 1)
        self.assertEqual(Calculator.divide(100, -10), -10)
        self.assertEqual(Calculator.divide(-50, -50), 1)
        self.assertRaises(ValueError, Calculator.divide, 5, 0)
        self.assertEqual(Calculator.divide(8, 2), 4)
