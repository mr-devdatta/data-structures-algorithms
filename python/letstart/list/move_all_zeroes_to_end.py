lst = [1, 2, 0, 4, 3, 0, 5, 0]
#Output: [1, 2, 4, 3, 5, 0, 0, 0]

lst1 = [ i for i in lst if i > 0 ] + [0] * lst.count(0)
print(lst1)
