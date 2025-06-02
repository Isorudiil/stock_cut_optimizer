import math

class StockMaterial:
    def __init__(self, name, length, quantity):
        self.name = name
        self.length = length
        self.quantity = quantity

    def __str__(self):
        return f'Name: {self.name} || Length: {self.length}" ({math.floor(self.length/12)}ft-{self.length % 12}in) || Quantity: {self.quantity}'
        

class CutMaterial:
    def __init__(self, name, length, quantity):
        self.name = name
        self.length = length
        self.quantity = quantity

    def __str__(self):
        return f'Name: {self.name} || Length: {self.length}" || Quantity: {self.quantity}'
