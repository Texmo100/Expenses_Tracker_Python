from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from src.expenses_tracker.models.CategoryList import CategoryList
from src.expenses_tracker.models.Category import Category

class TestCategoryList(TestCase):
    def setUp(self):
        self.obj = CategoryList()

    def tearDown(self):
        self.obj = None

    def test_categorylist_initialization(self):
        self.assertIsInstance(self.obj, CategoryList)
        self.assertIsInstance(self.obj.collection, list)
    
    def test_categorylist_add_with_valid_values(self):
        new_category = Category()
        self.obj.add_to_list(new_category)

        self.assertIn(new_category, self.obj.collection)

    @patch("sys.stdout", new_callable=StringIO)
    def test_categorylist_add_with_invalid_values(self, mock_stdout):
        fake_category = "fake category"
        self.obj.add_to_list(fake_category)

        error_messages = mock_stdout.getvalue().split("\n")

        self.assertIn("Operation not allowed (Add): The new item is not a category", error_messages)

    def test_categorylist_select_from_list_by_name(self):
        new_category = Category("games", "This is a dummy description", 1000.0)
        self.obj.add_to_list(new_category)

        selected_category_by_name = self.obj.select_from_list_by_name("games")

        self.assertEqual(selected_category_by_name, new_category)

    @patch("sys.stdout", new_callable=StringIO)
    def test_categorylist_print_list(self, mock_stdout):
        new_category = Category("games", "This is a dummy description", 1000.0)
        self.obj.add_to_list(new_category)

        self.obj.print_list()

        messages = mock_stdout.getvalue().split("\n")

        self.assertIn(f'ID: {self.obj.collection[0].id}', messages)
        self.assertIn(f'Name: {self.obj.collection[0].name}', messages)
        self.assertIn(f'Description: {self.obj.collection[0].description}', messages)
        self.assertIn(f'Budget Limit: {self.obj.collection[0].limit}', messages)

    def test_categorylist_remove(self):
        category = Category("games", "This is a dummy description", 1000.0)
        self.obj.add_to_list(category)

        self.obj.remove_from_list(category)

        self.assertNotIn(category, self.obj.collection)

    @patch("sys.stdout", new_callable=StringIO)
    def test_categorylist_remove_no_valid_items(self, mock_stdout):
        fake_category = "fake category"
        self.obj.remove_from_list(fake_category)

        error_messages = mock_stdout.getvalue().split("\n")

        self.assertIn("Operation not allowed (Delete): The new item is not a category", error_messages)
