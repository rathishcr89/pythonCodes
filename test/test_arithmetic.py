
import unittest
from Arithmetic import readInpu, sum, mul, minus, divide, divide2, modulo
from unittest.mock import patch

class TestArithmeticOperations(unittest.TestCase):

  
    def test_sum(self):
        self.assertEqual(sum(10, 5), 15)

    def test_sum(self):
        self.assertEqual(sum(10, 2), 15)

    def test_mul(self):
        self.assertEqual(mul(10, 5), 50)

    def test_minus(self):
        self.assertEqual(minus(10, 5), 5)

    def test_divide(self):
        self.assertAlmostEqual(divide(10, 4), 2.5)

    def test_divide2(self):
        self.assertEqual(divide2(10, 4), 2)

    def test_modulo(self):
        self.assertEqual(modulo(10, 4), 2)

if __name__ == '__main__':
    unittest.main()
