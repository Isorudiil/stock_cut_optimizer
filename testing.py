from material_class import CutMaterial, StockMaterial


"""# cut_list = []

# new_cut = material.CutMaterial('SP20080-00', 15.75, 50)
# cut_list.append(new_cut)
# new_cut = material.CutMaterial('SP20037-08', 10.125, 1000)
# cut_list.append(new_cut)

# print(cut_list[0].length)
# sorted_cut = sorted(cut_list, key=lambda cut_part: cut_part.length, reverse=True)
# for cut in sorted_cut:
#     print(cut)"""


"""cut_list = []

cut_0 = CutMaterial("SP20037-00", 10, 50)
cut_1 = CutMaterial("SP20037-01", 10.125, 100)
cut_2 = CutMaterial("SP20037-02", 10.125, 25)
cut_3 = CutMaterial("SP20037-03", 24.125, 40)
cut_4 = CutMaterial("SP20037-04", 7.4375, 625)
cut_5 = CutMaterial("SP20037-05", 7.125, 300)
cut_6 = CutMaterial("SP20037-06", 8.5, 750)

for i in range(7):
    cut_list.append(str("cut_" + str(i)))

print(cut_list)"""

"""# cut_0 = CutMaterial("SP20037-00", 10, 50)
# cut_1 = CutMaterial("SP20037-01", 10.125, 100)
# cut_2 = CutMaterial("SP20037-02", 10.125, 25)
# cut_3 = CutMaterial("SP20037-03", 24.125, 40)
# cut_4 = CutMaterial("SP20037-04", 7.4375, 625)
# cut_5 = CutMaterial("SP20037-05", 7.125, 300)
# cut_6 = CutMaterial("SP20037-06", 8.5, 750)

# cut_list = [cut_0, cut_1, cut_2, cut_3, cut_4, cut_5, cut_6]

# stock_0 = StockMaterial("SP0003713", 240, 20)
# stock_1 = StockMaterial("SP0003713", 120, 20)
# stock_2 = StockMaterial("SP0003713", 360, 20)

# stock_list = [stock_0, stock_1, stock_2]

# for stock in stock_list:
#     while stock.quantity > 0:
#         print(stock.quantity)
#         stock.quantity -= 1"""

cut_0 = CutMaterial("SP20037-00", 60, 50)
cut_1 = CutMaterial("SP20037-03", 36, 40)

temp_cut_list = [cut_0, cut_1,]

stock_0 = StockMaterial("SP0003713", 360, 20)

temp_stock_list = [stock_0,]

for stock in temp_stock_list:
    while stock.quantity > 0:
        while stock.length > 0:
            for cut in range(len(temp_cut_list)):
                if temp_cut_list[cut].length < stock.length:
                    print("This is temp cut list %i length: %i" % (cut, temp_cut_list[cut].length))
                    print("This is temp stock length on iteration %i: %i" % (cut, stock.length))
                    temp_cut_list[cut].quantity -= 1
                    stock.length -= temp_cut_list[cut].length
                    print("This is stock length after subtract: %i" % stock.length)
                    print("This is the remaining cuts for cut %i: %i" % (cut, temp_cut_list[cut].quantity))
                    print("------")
                    break
                else:
                    break
