"""
Tube cut optimizer
Designed to solve the cutting stock problem

- Elijah Herald
"""


"""
Inputs:
- Stock size(s)
- Stock quantity
- Cut size(s)
- Cut quantities
- Maybe some machine parameters to help nest for a specific machine?

Outputs:
- Total quantity of tubes needed
- Total scrap
- Avg. scrap length?
- "Nest" layouts
- Quantity of each "nest"

General program process:
- Input stock sizes, qtys, cut sizes, cut qtys, and possibly machine parameters
- Organize stock sizes and quantities in maybe a list of dictionaries where the value is a tuple
    - Option 1: list of dictionaries where key is a stock name and value is a tuple of length and qty
        - [{"SP0003025-3600": (360, 100)}, {"SP0003025-2400": (240, 50)}]
    - Option 2: list of tuples of length and quantity; can only manage one stock per run
        - [(360, 100), (240, 50)]
    - Option 3:
        - [{"SP0003025-3600": [{"Length": 360}, {"Quantity": 100}]}, {"SP0003025-2400": [{"Length": 240}, {"Quantity": 50}]}]
- Organize cut sizes and quantities in maybe a dictionary of dictionaries?
    - Option 1: list of tuples of length and quantity; would only work with one stock per run
        - [(120, 80), (60, 40)]
    - Option 2
        - [{"SP1003025-1200L": (120, 80)}, {"SP1003025-0600": (60, 40)}]
- Algorithmically remove quantities from cut sizes and stock quantities to maintain remaining stock and needed to cut
    - Would need to maintain original data and create new dictionaries/lists/tuples while data is running and output to a new dataset
- Output total quantity of tubes, total scrap, avg scrap, "nest" layouts, and quantity of each "nest" layout
"""

from material_class import StockMaterial

def stock_parts():
    stock = []
    more_stock = True

    while more_stock == True:
        stock_name = input("What is your stock material called?\n")
        stock_length = input("How long is your stock length?\n")
        stock_quantity = input("How many pieces of %s do you have?\n" % stock_name)
        stock_dict = {stock_name: [{"Length": int(stock_length)}, {"Quantity": int(stock_quantity)}]}
        stock.append(stock_dict)

        while True:
            more = input("Do you have more stock to input? (yes or no)\n")
            if more.lower() == 'y' or more.lower() == 'yes':
                more_stock = True
                break
            elif more.lower() == 'n' or more.lower() == 'no':
                more_stock = False
                return stock
            else:
                print("You did not input 'yes' or 'no'. Please try again.")


if __name__ == '__main__':
    while True:
        options = [1, 2, 3, 4, 5, 6, 7,]
        print("\nWhat would you like to do? (Type the number)\n")
        print("1. Add stock material")
        print("2. Add to cut list")
        print("3. View stock materials list")
        print("4. View cut materials list")
        print("5. View stock and cut materials list")
        print("6. Nest using longest parts first")
        print("7. Exit program\n")

        stock_list

        number = int(input())
        if number not in options:
            print("You either entered an invalid number\nor did not enter a number at all\n")
        elif number == 1:
            stock_list = stock_parts()
        elif number == 2:
            pass
        elif number == 3:
            try:
                print("\n     *********      ")
                print("Here is your current stock:")
                print(stock_list)
                print("     *********      \n")
            except NameError:
                print("\n      *********     ")
                print("You have no stock yet!")
                print("      *********     \n")

        elif number == 4:
            pass
        elif number == 5:
            pass
        elif number == 6:
            pass
        elif number == 7:
            print("    *********    ")
            print("Have a great day!")
            print("    *********    ")
            break
