import unittest
from discount import *

class DiscountTest(unittest.TestCase):

    def test_purchase_total_is_10(self):
        discount = Discount()
        result_actual = discount.get_discount(10)

        self.assertEqual(0, result_actual)

    def test_purchase_total_is_11(self):
        discount = Discount()
        result_actual = discount.get_discount(11)

        self.assertEqual(10, result_actual)

    def test_purchase_total_is_21(self):
        discount = Discount()
        result_actual = discount.get_discount(21)

        self.assertEqual(20, result_actual)

if __name__ == '__main__':
    unittest.main()