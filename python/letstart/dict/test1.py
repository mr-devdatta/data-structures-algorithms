data = [
    ["john", 94],
    ["alis", 90],
    ["dave", 74],
    ["john", 74],
    ["john", 90],
]

dct = {}

for row in data:
    #print(row[0])

    if row[0] not in dct:
        dct[row[0]] = [row[1]]
    else:
        #avg = sum(dct.get(row[0]) + [row[1]]) / len(dct.get(row[0]) + [row[1]])
        dct[row[0]] = dct.get(row[0]) + [row[1]]

print(dct)

dct1 = {}
for elent in dct.items():
    lst = elent[1]
    dct1[elent[0]] = [sum(lst) / len(lst)]

print(dct1)

