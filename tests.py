import unittest
from format_price import format_price

class TestFormatPrice(unittest.TestCase):

    def test_valid_string_input(self):
        self.assertEqual(format_price('3245.000000'), '3 245')
        self.assertEqual(format_price('3245'), '3 245')
        self.assertEqual(format_price('3245.6'), '3 245.6')
        self.assertEqual(format_price('3245.67'), '3 245.67')
        self.assertEqual(format_price('3245.678'), '3 245.68')
        self.assertEqual(format_price('0'), '0')
        self.assertEqual(format_price('0.1'), '0.1')
        self.assertEqual(format_price('0.12'), '0.12')
        self.assertEqual(format_price('0.123'), '0.12')
        self.assertEqual(format_price('0.1234'), '0.12')

    def test_number_input(self):
        self.assertEqual(format_price(3245.000000), '3 245')
        self.assertEqual(format_price(3245), '3 245')
        self.assertEqual(format_price(3245.6), '3 245.6')
        self.assertEqual(format_price(3245.67), '3 245.67')
        self.assertEqual(format_price(3245.678), '3 245.68')
        self.assertEqual(format_price(0), '0')
        self.assertEqual(format_price(0.1), '0.1')
        self.assertEqual(format_price(0.12), '0.12')
        self.assertEqual(format_price(0.123), '0.12')
        self.assertEqual(format_price(0.1234), '0.12')

    def test_invalid_input(self):
        self.assertEqual(format_price('123qwer'), None)
        self.assertEqual(format_price('qwerqwasdf'), None)
        self.assertEqual(format_price('1234123,123'), None)
        self.assertEqual(format_price('qw1212r'), None)
        self.assertEqual(format_price(',2314'), None)
        self.assertEqual(format_price({}), None)
        self.assertEqual(format_price([]), None)
        self.assertEqual(format_price(format_price), None)
        self.assertEqual(format_price(format_price(None)), None)

if __name__ == '__main__':
    unittest.main()