import unittest
import decimal
from format_price import format_price


class TestFormatPrice(unittest.TestCase):

    # Valid string cases
    def test_valid_string_input1(self): self.assertEqual(
        format_price('3245.000000'), '3 245')

    def test_valid_string_input2(self): self.assertEqual(
        format_price('3245'), '3 245')

    def test_valid_string_input3(self): self.assertEqual(
        format_price('3245.6'), '3 245.6')

    def test_valid_string_input4(self): self.assertEqual(
        format_price('3245.67'), '3 245.67')

    def test_valid_string_input5(self): self.assertEqual(
        format_price('3245.678'), '3 245.68')

    def test_valid_string_input6(
        self): self.assertEqual(format_price('0'), '0')

    def test_valid_string_input7(self): self.assertEqual(
        format_price('0.1'), '0.1')

    def test_valid_string_input8(self): self.assertEqual(
        format_price('0.12'), '0.12')

    def test_valid_string_input9(self): self.assertEqual(
        format_price('0.123'), '0.12')

    def test_valid_string_input10(self): self.assertEqual(
        format_price('0.1234'), '0.12')

    # Valid non-string cases
    def test_number_input1(self): self.assertEqual(
        format_price(3245.000000), '3 245')

    def test_number_input2(self): self.assertEqual(format_price(3245), '3 245')

    def test_number_input3(self): self.assertEqual(
        format_price(3245.6), '3 245.6')

    def test_number_input4(self): self.assertEqual(
        format_price(3245.67), '3 245.67')

    def test_number_input5(self): self.assertEqual(
        format_price(3245.678), '3 245.68')

    def test_number_input6(self): self.assertEqual(format_price(0), '0')

    def test_number_input7(self): self.assertEqual(format_price(0.1), '0.1')

    def test_number_input8(self): self.assertEqual(format_price(0.12), '0.12')

    def test_number_input9(self): self.assertEqual(format_price(0.123), '0.12')

    def test_number_input10(self): self.assertEqual(
        format_price(0.1234), '0.12')

    def test_number_input11(self): self.assertEqual(
        format_price(format_price(decimal.Decimal(2))), '2')

    def test_number_input12(self): self.assertEqual(
        format_price(format_price(decimal.Decimal(2.1))), '2.1')

    # Invalid cases
    def test_invalid_input1(self): self.assertEqual(
        format_price('123qwer'), None)

    def test_invalid_input2(self): self.assertEqual(
        format_price('qwerqwasdf'), None)

    def test_invalid_input3(self): self.assertEqual(
        format_price('1234123,123'), None)

    def test_invalid_input4(self): self.assertEqual(
        format_price('qw1212r'), None)

    def test_invalid_input5(self): self.assertEqual(
        format_price(',2314'), None)

    def test_invalid_input6(self): self.assertEqual(format_price({}), None)

    def test_invalid_input7(self): self.assertEqual(format_price([]), None)

    def test_invalid_input8(self): self.assertEqual(
        format_price(format_price), None)

    def test_invalid_input9(self): self.assertEqual(
        format_price(format_price(None)), None)

    def test_invalid_input10(self): self.assertEqual(
        format_price(format_price(True)), None)


if __name__ == '__main__':
    unittest.main()
