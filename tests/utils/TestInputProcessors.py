import unittest
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from src.expenses_tracker.utils.helpers import *
from src.expenses_tracker.utils.input_processors import *

class TestInputProcessors(TestCase):
    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_option_input_processor_with_empty_input_then_valid_input(self, mock_stdout, mock_input):
        mock_input.side_effect = ["        ", "4"]

        actual_result = option_input_processor("Enter an option: ", num_options=4)
        messages = mock_stdout.getvalue().split("\n")

        self.assertIn("Input not valid: This is only white spaces or is an empty string", messages)
        self.assertEqual(actual_result, 4)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_option_input_processor_with_invalid_input_then_valid_input(self, mock_stdout, mock_input):
        mock_input.side_effect = ["hello879dahdua&(*)", "4"]

        actual_result = option_input_processor("Enter an option: ", num_options=4)
        messages = mock_stdout.getvalue().split("\n")

        self.assertIn("Something went wrong: Enter numbers only", messages)
        self.assertEqual(actual_result, 4)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_option_input_processor_with_invalid_num_options_then_valid_num_options(self, mock_stdout, mock_input):
        mock_input.side_effect = ["5", "4"]

        actual_result = option_input_processor("Enter an option: ", num_options=4)
        messages = mock_stdout.getvalue().split("\n")

        self.assertIn("Input is out of range of available options", messages)
        self.assertEqual(actual_result, 4)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_string_input_processor_with_empty_input_then_valid_input(self, mock_stdout, mock_input):
        mock_input.side_effect = ["   ", "hello"]
        actual_result = string_input_processor("Enter your string: ")
        self.assertIn("Input not valid: This is only white spaces or is an empty string", mock_stdout.getvalue())
        self.assertEqual(actual_result, "hello")

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_string_input_processor_with_invalid_input_then_valid_input(self, mock_stdout, mock_input):
        mock_input.side_effect = ["", "hello"]
        actual_result = string_input_processor("Enter your string: ")
        self.assertIn("Input not valid: This is only white spaces or is an empty string", mock_stdout.getvalue())
        self.assertEqual(actual_result, "hello")

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_float_input_processor_with_empty_input_then_valid_input(self, mock_stdout, mock_input):
        mock_input.side_effect = ["    ", "42.56"]
        actual_result = float_input_processor("Enter your currency")
        self.assertIn("Input not valid: This is only white spaces or is an empty string", mock_stdout.getvalue())
        self.assertEqual(actual_result, 42.56)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_float_input_processor_with_invalid_input_then_valid_input(self, mock_stdout, mock_input):
        mock_input.side_effect = ["helllo", "34.89"]
        actual_result = float_input_processor("Enter your currency: ")
        self.assertIn("Something went wrong: Enter numbers only", mock_stdout.getvalue())
        self.assertEqual(actual_result, 34.89)

    @patch("builtins.input")
    @patch("sys.stdout", new_callable=StringIO)
    def test_float_input_processor_with_zero_then_valid_input(self, mock_stdout, mock_input):
        mock_input.side_effect = ["0", "34.89"]
        actual_result = float_input_processor("Enter your currency: ")
        self.assertIn("Input not valid: This might be zero. Enter just floating numbers only", mock_stdout.getvalue())
        self.assertEqual(actual_result, 34.89)

if __name__ == "__main__":
    unittest.main()
