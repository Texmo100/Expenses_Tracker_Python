import unittest
from ..utils.helpers import *

class TestHelpers(unittest.TestCase):
    def test_is_valid_string_with_string(self):

        # Arrange
        value_to_test = "hello"

        # Act
        actual_result = is_valid_string(value_to_test)

        # Assert
        self.assertTrue(actual_result)

    def test_is_valid_string_with_non_string(self):
        value_to_test = 23
        actual_result = is_valid_string(value_to_test)
        self.assertFalse(actual_result)

    def test_is_valid_text_with_large_string(self):
        value_to_test = """This is a large text with empty spaces and all kind of characters in it 809808183209123131];]['']"""
        actual_result = is_valid_text(value_to_test)
        self.assertTrue(actual_result)

    def test_is_valid_text_with_word(self):
        value_to_test = "hello"
        actual_result = is_valid_text(value_to_test)
        self.assertFalse(actual_result)

    def test_is_valid_phone_number_with_digits(self):
        value_to_test = "6623456517"
        actual_result = is_valid_phone_number(value_to_test)
        self.assertTrue(actual_result)

    def test_is_valid_phone_number_with_special_characters(self):
        value_to_test = "6623-4565-17"
        actual_result = is_valid_phone_number(value_to_test)
        self.assertFalse(actual_result)

    def test_is_valid_integer_with_numbers(self):
        value_to_test = 34
        actual_result = is_valid_integer(value_to_test)
        self.assertTrue(actual_result)

    def test_is_valid_integer_with_string(self):
        value_to_test = "hello345"
        actual_result = is_valid_integer(value_to_test)
        self.assertFalse(actual_result)

    def test_is_valid_currency_with_currency(self):
        value_to_test = 34.56
        actual_result = is_valid_currency(value_to_test)
        self.assertTrue(actual_result)

    def test_is_valid_currency_with_simple_number(self):
        value_to_test = 100
        actual_result = is_valid_currency(value_to_test)
        self.assertFalse(actual_result)

if __name__ == "__main__":
    unittest.main()
