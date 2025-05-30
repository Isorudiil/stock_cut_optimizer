import math

class StockMaterial:
    stock_list = []
    def __init__(self, name, length, quantity):
        StockMaterial.stock_list.append(self)
        self.name = name
        self.length = length
        self.quantity = quantity

    def __str__(self):
        return f'Name: {self.name} || Length: {self.length}" ({math.floor(self.length/12)}ft-{self.length % 12}in) || Quantity: {self.quantity}'
    

# material = input("What is your material called?\n")
# length = input("How long is your material?\n")
# quantity = input("How many pieces of %s do you have?\n" % material)

# new_stock = StockMaterial(material, int(length), int(quantity))
