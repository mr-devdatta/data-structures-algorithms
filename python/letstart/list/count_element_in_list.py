
lst = [10, 11, 22, 33, 44, 44, 55, 66, 77, 22, 11, 88, 99, 11]
print(lst)


print(" ----  Using SET --------")
lsSet = set(lst)
print(lsSet)

dct = {}
for i in lsSet:
    dct[i] = lst.count(i)
print(dct)


print(" ----  Using dictionary --------")
dct = {}
for i in lst:
    dct[i] = dct.get(i, 0) + 1

print(dct)
