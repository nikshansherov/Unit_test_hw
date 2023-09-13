import unittest
from decimal import Decimal


class Calculator:
    def __init__(self):
        pass

    def calculate_discount(self, amount_without_discount, discount_percentage):
        try:
            amount = Decimal(amount_without_discount - (amount_without_discount * discount_percentage / 100))
            amount = amount.quantize(Decimal('1.00'))
            return {'amount_without_discount': amount_without_discount,
                    'discount_percentage': discount_percentage, 'amount': amount}
        except TypeError:
            print('входные данные не являются числом')


class TestCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_calculate_discount_arithmetic(self):
        amount = self.calculator.calculate_discount(100, 10)['amount']
        self.assertEqual(amount, 90)

    def test_calculate_discount_negative(self):
        amount = self.calculator.calculate_discount(100, 10)['amount']
        self.assertTrue(amount > 0), \
            'итоговая сумма не может быть отрицательной или нулевой'

    def test_calculate_discount_argument_amount(self):
        amount_without_discount = self.calculator.calculate_discount(100, 10)['amount_without_discount']
        self.assertTrue(amount_without_discount > 0), 'Входная сумма не может быть меньше или равной 0'

    def test_calculate_discount_argument_discount_percentage(self):
        discount_percentage = self.calculator.calculate_discount(100, 10)['discount_percentage']
        self.assertTrue(discount_percentage >= 0 and discount_percentage <= 100), 'Процент скидки должен быть' \
                                                                                  ' в пределах от 0 до 100'


if __name__ == '__main__':
    unittest.main()
