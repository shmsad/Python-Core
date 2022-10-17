#flattern the list of list
li = [[1,2,3],[4,5,6],[7,8,9]]
l1 = [y for x in li for y in x]
print(l1)
l2 = []
for i in li:
    for j in i:
        l2.append(j)
print(l2)