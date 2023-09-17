import unittest
from number_in_interval import number_in_interval


class TestNumberInInterval(unittest.TestCase):
    def test_number_in_interval_type(self):
        self.assertRaisesRegex(ValueError, 'Введеное значение должно быть числом',
                               number_in_interval, n='')

    def test_number_in_interval_true(self):
        self.assertTrue(number_in_interval(30))

    def test_number_in_interval_false(self):
        self.assertFalse(number_in_interval(110))
        self.assertFalse(number_in_interval(10))
