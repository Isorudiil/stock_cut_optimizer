import unittest
from main import base_questions, material_list, nest_longest_parts_first, main_loop
from material_class import CutMaterial, StockMaterial

class TestMainModule(unittest.TestCase):
    
    def test_cut_list_sorting():
        cut_0 = CutMaterial("SP20037-00", 10, 50)
        cut_1 = CutMaterial("SP20037-01", 10.125, 100)
        cut_2 = CutMaterial("SP20037-02", 10.125, 25)
        cut_3 = CutMaterial("SP20037-03", 24.125, 40)
        cut_4 = CutMaterial("SP20037-04", 7.4375, 625)
        cut_5 = CutMaterial("SP20037-05", 7.125, 300)
        cut_6 = CutMaterial("SP20037-06", 8.5, 750)

        cut_list = [cut_0, cut_1, cut_2, cut_3, cut_4, cut_5, cut_6]

        stock_0 = StockMaterial("SP0003713", 240, 20)
        stock_1 = StockMaterial("SP0003713", 120, 20)
        stock_2 = StockMaterial("SP0003713", 360, 20)

        stock_list = [stock_0, stock_1, stock_2]

        nest_longest_parts_first(stock_list, cut_list)


        