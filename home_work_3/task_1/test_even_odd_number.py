import unittest
from even_odd_number import even_odd_number


class TestEvenOddNumber(unittest.TestCase):
    def test_even_odd_number_type(self):
        self.assertRaisesRegex(ValueError, 'Введеное значение должно быть числом',
                               even_odd_number, n='')

    def test_even_odd_number_even(self):
        self.assertTrue(even_odd_number(4))

    def test_even_odd_number_odd(self):
        self.assertFalse(even_odd_number(5))
