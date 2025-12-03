import unittest
from unittest import TestCase
from unittest.mock import patch
from src.expenses_tracker.utils.helpers import *
from src.expenses_tracker.models.Category import Category

class TestHelpers(TestCase):
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

    def test_is_valid_name_in_collection_with_no_existing_name(self):
        category = Category("Games", "description for category", 100.0)
        test_category_list = [category]

        test_name = "Home"

        self.assertTrue(is_valid_name_in_collection(test_name, test_category_list))

    def test_is_valid_name_in_collection_with_existing_name(self):
        category = Category("Games", "description for category", 100.0)
        test_category_list = [category]

        test_name = "Games"

        self.assertFalse(is_valid_name_in_collection(test_name, test_category_list))

    @patch("builtins.print")
    def test_is_valid_name_in_collection_with_no_valid_collection_type(self, mock_print):
        test_category_list = "test category list"

        test_name = "Games"

        self.assertFalse(is_valid_name_in_collection(test_name, test_category_list))
        mock_print.assert_called_once_with("The collection is not a list or there are no items in it")

    @patch("builtins.print")
    def test_is_valid_name_in_collection_with_invalid_items(self, mock_print):
        test_category_list = ["category_01", "category_02"]

        test_name = "Games"

        self.assertFalse(is_valid_name_in_collection(test_name, test_category_list))
        mock_print.assert_called_once_with("Something went wrong during this operation: Attribute Error was detected")

if __name__ == "__main__":
    unittest.main()
