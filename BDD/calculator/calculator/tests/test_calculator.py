
from ..calculator import Calculator
import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(4, self.calc.add(2,2))
