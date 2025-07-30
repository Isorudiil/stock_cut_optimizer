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

cut_list = [cut_0, cut_1]
temp_cut_list = [cut_0, cut_1,]

stock_0 = StockMaterial("SP0003713", 363, 20)

stock_list = [stock_0,]
temp_stock_list = [stock_0,]
drop_list = []

for stock in temp_stock_list:
    while stock.quantity > 0:
        temp_stock_length = stock.length
        for cut in range(len(temp_cut_list)):
            while temp_cut_list[cut].length < temp_stock_length and temp_cut_list[cut].quantity > 0:
                print("This is temp cut list %i length: %i" % (cut, temp_cut_list[cut].length))
                print("This is temp stock length on iteration %i: %i" % (cut, temp_stock_length))
                temp_cut_list[cut].quantity -= 1
                temp_stock_length -= temp_cut_list[cut].length
                print("This is stock length after subtract: %i" % temp_stock_length)
                print("This is the remaining cuts for cut %i: %i" % (cut, temp_cut_list[cut].quantity))
                print("------")
        if temp_stock_length > 60:
            stock.quantity -= 1
            drop_list.append(temp_stock_length)
            break
        else:
            drop_list.append(temp_stock_length)
            stock.quantity -= 1
            print(f"This is the remaining stock quantity: {stock.quantity}")
            print("------")

print("\n")
print("******\n")
print("Cuts remaining:")
print([(temp_cut_list[x].name, temp_cut_list[x].quantity) for x in range(len(temp_cut_list))])
print("\n")
print(temp_stock_list[0])
print(f"\nDrops from {stock.name}:")
print(drop_list)
print(f"\nTotal sum of drops from {stock.name}:")
print(sum(drop_list))
print("\n******")
