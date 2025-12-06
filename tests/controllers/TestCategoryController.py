from unittest import TestCase
from unittest.mock import patch, MagicMock
from src.expenses_tracker.controllers.CategoryController import CategoryController
from src.expenses_tracker.models.Category import Category
from src.expenses_tracker.models.CategoryList import CategoryList

class TestCategoryController(TestCase):
    def setUp(self):
        self.obj = CategoryController()

    def tearDown(self):
        self.obj = None

    @patch("builtins.print")
    @patch.object(CategoryController, "_fill_info")
    def test_create_success(self, mock_fill_info, mock_print):
        new_category = self.obj.create()

        self.assertIsInstance(new_category, Category)
        mock_fill_info.assert_called_once_with(new_category)
        mock_print.assert_called_once_with("New Category created sucessfully!")

    @patch("builtins.print")
    @patch.object(CategoryController,"_fill_info")
    def test_update_success(self, mock_fill_info, mock_print):
        category = MagicMock(spec=Category)
        self.obj.update(category)

        mock_fill_info.assert_called_once_with(category)
        mock_print.assert_called_once_with("Category updated sucessfully!")

    @patch("src.expenses_tracker.controllers.CategoryController.is_valid_name_in_collection")
    @patch("src.expenses_tracker.controllers.CategoryController.float_input_processor")
    @patch("src.expenses_tracker.controllers.CategoryController.string_input_processor")
    def test_fill_info_with_valid_values(self, mock_string_processor, mock_float_procesor, mock_validname):
        category = MagicMock(spec=Category)
        mock_categorylist = MagicMock(spec=CategoryList)
        mock_string_processor.side_effect = ["Games", "long description for category"]
        mock_float_procesor.return_value = 1000.0
        mock_validname.return_value = True

        self.obj._fill_info(category, mock_categorylist)

        self.assertEqual(category.name, "Games")
        self.assertEqual(category.description, "long description for category")
        self.assertEqual(category.limit, 1000.0)

        mock_string_processor.assert_any_call("Enter the category name: ")
        mock_string_processor.assert_any_call("Enter the category description: ")
        mock_float_procesor.assert_called_once_with("Enter the category limit: ")
