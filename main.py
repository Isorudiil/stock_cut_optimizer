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

import material_class as m_c
import pyinputplus as pyip


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
    print("\n------")
    print("Have a great day!")
    print("------")

def base_questions(option): # basic questions that apply to stock and cut material
    if option == 1:
        operation = 'material'
    elif option == 2:
        operation = 'cut piece'
    
    material = pyip.inputStr("What is your %s called?\n" % operation)
    length = pyip.inputNum("How long is your %s?\n" % operation)
    if option == 1:
        quantity = pyip.inputNum("How many pieces of %s do you have?\n" % material)
    elif option == 2:
        quantity = pyip.inputNum("How many pieces of %s do you have to cut?\n" % material)

    return (material, length, quantity)

def material_list(option, stock_materials, cut_materials): # try block to view a material list, if it exists
    if option == 3:
        operation = 'stock'
    elif option == 4:
        operation = 'cut list'
    elif option == 5:
        operation = 'stock and cut list'
        
    print("\n------")
    print("Here is your current %s:" % operation)
    if option == 3:
        for material in stock_materials:
            print(material)
    elif option == 4:
        for material in cut_materials:
            print(material)
    elif option == 5:
        print("Stock:")
        for material in stock_materials:
            print(material)
        print("\nCut:")
        for material in cut_materials:
            print(material)
    print("------\n")

def nest_longest_parts_first(stock_list, cut_list):
    print("\nAttempting to nest with:")
    print("------")
    print("Stock materials:")
    for stock in stock_list:
        print(stock)
    print("\nCut materials:")
    for cut in cut_list:
        print(cut)
    print("------")

    """ Pseudocode
    Sort cut_list in descending order
    For loop to iterate through qty of stock_list
    While loop to fit from cut_list until no more can fit
    * Can I fit a smaller piece on if I know it will fit better?
    """

    cut_list.sort(key=lambda cut_part: cut_part.length, reverse=True)
    print("\n------")
    print("Sorted by length (descending):")
    for part in cut_list:
        print(part)    
    print("------")

    temp_cut_list = cut_list
    temp_stock_list = stock_list

    for stock in temp_stock_list:
        while stock.quantity > 0:
            while stock.length > 0:
                temp_stock_length = stock.length
                for length in temp_cut_list.length:
                    if length < temp_stock_length:
                        temp_cut_list[length].qty -= 1
                        break

def main_loop(): # main program loop
    all_stock_materials = []
    all_cut_materials = []

    while True:
        options = [1, 2, 3, 4, 5, 6, 7,]
        hello()

        number = pyip.inputInt(greaterThan=0, lessThan=8)
        if 0 < number < 3:
            material_info = base_questions(number)
            if number == 1:
                new_stock = m_c.StockMaterial(*material_info)
                all_stock_materials.append(new_stock)
                print(f"\nAdded: {new_stock.quantity} pieces of {new_stock.name} ({new_stock.length}in)\n")
            elif number == 2:
                new_cut = m_c.CutMaterial(*material_info)
                all_cut_materials.append(new_cut)
                print(f"\nAdded: {new_cut.quantity} pieces of {new_cut.name} ({new_cut.length}in) to cut list\n")
        elif 2 < number < 6:
            material_list(number, all_stock_materials, all_cut_materials)
        elif number == 6:
            nest_longest_parts_first(all_stock_materials, all_cut_materials)
        elif number == 7:
            goodbye()
            break


if __name__ == '__main__':
    main_loop()
