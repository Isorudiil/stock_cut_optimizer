""" Stock Cutting Optimizer
Designed to solve the cutting stock problem

- Elijah Herald
"""


""" Pseudocode/Flowcharting
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

import material_class

# def stock_parts(option): # loops through the stock part creation sequence
#     # if option == 1:
#     #     temp = "stock material"
#     # elif option == 2:
#     #     temp = "cut material"

#     # if stock or cut:
#     #     print("You have already entered %s, would you like to enter more?" % temp)

#     # if option == 1:
#     stock = []
#     # elif option == 2:
#     #     cut = []
#     more_stock = True

#     while more_stock == True:
#         name = input("What is your stock material called?\n")
#         length = input("How long is your stock length?\n")
#         quantity = input("How many pieces of %s do you have?\n" % name)
#         init_dict = {name: [{"Length": int(length)}, {"Quantity": int(quantity)}]}
#         stock.append(init_dict)

#         while True:
#             more = input("Do you have more stock to input? (yes or no)\n")
#             if more.lower() == 'y' or more.lower() == 'yes':
#                 more_stock = True
#                 break
#             elif more.lower() == 'n' or more.lower() == 'no':
#                 more_stock = False
#                 return stock
#             else:
#                 print("You did not input 'yes' or 'no'. Please try again.")

def hello(): # prints the opening message when the User starts the program
        print("\nWhat would you like to do? (Type the number)\n")
        print("1. Add stock material")
        print("2. Add to cut list")
        print("3. View stock materials list")
        print("4. View cut materials list")
        print("5. View stock and cut materials list")
        print("6. Nest using longest parts first")
        print("7. Exit program\n")

def goodbye(): # prints the exit message when the User requests to quit the program
    print("    *********    ")
    print("Have a great day!")
    print("    *********    ")

def base_questions(option): # basic questions that apply to stock and cut material
    if option == 1:
        operation = 'material'
    elif option == 2:
        operation = 'cut piece'
    
    material = input("What is your %s called?\n" % operation)
    length = float(input("How long is your %s?\n" % operation))
    if option == 1:
        quantity = int(input("How many pieces of %s do you have?\n" % material))
    elif option == 2:
        quantity = int(input("How many pieces of %s do you have to cut?\n" % material))

    return (material, length, quantity)

def main_loop(): # main program loop
    while True:
        options = [1, 2, 3, 4, 5, 6, 7,]
        hello()

        number = int(input())
        if number not in options:
            print("You either entered an invalid number\nor did not enter a number at all\n")
        elif number == 1:
            stock_info = base_questions(number)
            new_stock = material_class.StockMaterial(*stock_info)
        elif number == 2:
            stock_info = base_questions(number)
            new_cut = material_class.CutMaterial(*stock_info)
        elif number == 3:
            try:
                print("\n     *********      ")
                print("Here is your current stock:")
                print([str(material) for material in material_class.StockMaterial.stock_list])
                print("     *********      \n")
            except NameError:
                print("\n      *********     ")
                print("You have no stock yet!")
                print("      *********     \n")

        elif number == 4:
            try:
                print("\n     *********      ")
                print("Here is your current cut list:")
                print([str(material) for material in material_class.CutMaterial.cut_list])
                print("     *********      \n")
            except NameError:
                print("\n      *********     ")
                print("You have no cut list yet!")
                print("      *********     \n")
        elif number == 5:
            pass
        elif number == 6:
            pass
        elif number == 7:
            goodbye()
            break


if __name__ == '__main__':
    main_loop()