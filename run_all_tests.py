import unittest

# Utils
from tests.utils.TestHelpers import TestHelpers
from tests.utils.TestInputProcessors import TestInputProcessors

# Models
from tests.models.TestUser import TestUser
from tests.models.TestTracker import TestTracker
from tests.models.TestCategory import TestCategory
from tests.models.TestBudget import TestBudget
from tests.models.TestTransaction import TestTransaction
from tests.models.TestCategoryList import CategoryList
from tests.models.TestBudgetList import TestBudgetList
from tests.models.TestTransactionList import TransactionList

# Controllers
from tests.controllers.TestCategoryController import TestCategoryController
from tests.controllers.TestBudgetController import TestBudgetController

def create_suite():
    # Create a test suite
    suite = unittest.TestSuite()

    # Load modules
    loader = unittest.TestLoader()

    all_testcases = [
        TestHelpers,
        TestInputProcessors,
        TestUser,
        TestTracker,
        TestCategory,
        TestBudget,
        TestTransaction,
        CategoryList,
        TestBudgetList,
        TransactionList,
        TestCategoryController,
        TestBudgetController,
    ]

    for testcase in [all_testcases]:
        tests = loader.loadTestsFromTestCase(testcase)
        suite.addTests(tests)

    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(create_suite())
