import unittest

from app import calc


class TestCalc(unittest.TestCase):

    def test_multiply_3_by_2_should_return_6(self):
        self.assertEqual(6, calc.multiply(3, 2))

    def test_multiply_minus3_by_2_should_return_minus6(self):
        self.assertEqual(-6, calc.multiply(-3, 2))

    def test_multiply_1p75_by_2_should_return_3p5(self):
        self.assertEqual(3.5, calc.multiply(1.75, 2))

    def test_divide_1_by_2_should_return_0p5(self):
        self.assertEqual(0.5, calc.divide(1, 2))

if __name__ == '__main__':
    unittest.main()