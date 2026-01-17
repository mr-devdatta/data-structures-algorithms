lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#      [0,  1,  2,  3,  4,  5,  6,  7,  8,  9

cmp = [30, 60, 70]

allulululu = [  i*2 for i in lst if i in cmp and i % 3 == 0 ]
print(allulululu)



print(lst.index(50))
lst.insert(4, 90909090)
print(lst)