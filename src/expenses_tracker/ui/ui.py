def main_menu():
    print('Welcome to Expenses Tracker - Y')
    print('------------ Menu ------------')
    print('0: Exit')
    print('1: Categories menu ------------')
    print('2: Budgets menu ------------')
    print('3: Transactions menu ------------')
    print('-------------------------------')

def categories_menu(count):
    print('------------ Categories Menu ------------')
    print(f'Categories available: {count}')
    print('0: Main menu')
    print('1: Show categories')
    print('2: Create new category')
    print('3: Modify a category')
    print('4: Delete a Category')
    print('-----------------------------------------')

def budgets_menu(count):
    print('------------ Budgets Menu ------------')
    print(f'Budgets available: {count}')
    print('0: Main menu')
    print('1: Show budgets')
    print('2: Create new budget')
    print('3: Modify a budget')
    print('4: Delete a budget')
    print('-----------------------------------------')

def transactions_menu(count):
    print('------------ Transactions Menu ------------')
    print(f'Transactions available: {count}')
    print('0: Main menu')
    print('1: Show transactions')
    print('2: Create new transaction')
    print('3: Modify a transaction')
    print('4: Delete a transaction')
    print('-----------------------------------------')
