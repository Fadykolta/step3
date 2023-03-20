import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-2, 3), 1)
    
    def test_subtract(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(2, 3), -1)
        self.assertEqual(calc.subtract(-2, 3), -5)

if __name__ == '__main__':
    unittest.main()
