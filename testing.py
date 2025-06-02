import material_class as material

cut_list = []

new_cut = material.CutMaterial('SP20080-00', 15.75, 50)
cut_list.append(new_cut)
new_cut = material.CutMaterial('SP20037-08', 10.125, 1000)
cut_list.append(new_cut)

print(cut_list[0].length)
sorted_cut = sorted(cut_list, key=lambda cut_part: cut_part.length, reverse=True)
for cut in sorted_cut:
    print(cut)