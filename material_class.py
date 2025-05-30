class StockMaterial:

    def __init__(self, name, length, quantity):
        self.name = name
        self.length = length
        self.quantity = quantity

    def __repr__(self):
        return f"Name: {self.name}, Length (in inches): {self.length}, Quantity (in EA): {self.quantity}"