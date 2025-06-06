import unittest
from material_class import StockMaterial, CutMaterial

class TestMaterialClasses(unittest.TestCase):

    def test_stock_material_creation(self):
        """Test that StockMaterial objects are created correctly"""

        # create an instance of class
        stock = StockMaterial("SP0003025", 360, 10)

        # assertions to check if attributes are set correctly
        self.assertEqual(stock.name, "SP0003025")
        self.assertEqual(stock.length, 360)
        self.assertEqual(stock.quantity, 10)

    def test_stock_material_str_representation(self):
        """Test the __str__ method of StockMaterial"""
        
        # create an instance of class
        stock = StockMaterial("SP0002822U", 240, 3)

        # create a string that is formatted like __str__
        expected_str = 'Name: SP0002822U || Length: 240" (20ft-0in) || Quantity: 3'

        # assertion to check if string representation is set correctly
        self.assertEqual(str(stock), expected_str)

    def test_cut_material_creation(self):
        """Test that CutMaterial objects are created correctly"""

        # create an instance of class
        cut = CutMaterial("SP20030-00", 36, 15)

        # assertions to check if attributes are set correctly
        self.assertEqual(cut.name, "SP20030-00")
        self.assertEqual(cut.length, 36)
        self.assertEqual(cut.quantity, 15)

    def test_cut_material_str_representation(self):
        """Test the __str__ method of CutMaterial"""

        # create an instance of class
        cut = CutMaterial("SP20028-15", 15.125, 20)

        # create a string that is formatted like _str__
        expected_str = 'Name: SP20028-15 || Length: 15.125" || Quantity: 20'

        # assertion to check if string representation is set correctly
        self.assertEqual(str(cut), expected_str)

if __name__ == '__main__':
    unittest.main()
