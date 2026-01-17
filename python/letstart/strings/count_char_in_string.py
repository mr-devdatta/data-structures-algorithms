str = "Lenovo@DESKTOP-57CC8K9 MINGW64 /c/webroot/data-structures-algorithms/python/letstart (master)"

str = str.replace(" ", "").lower()
print(str)

dct1 = { char : str.count(char) for char in str  }
print(dct1)
print("")


dct2 = { char : str.count(char) for char in str if str.count(char) > 3 }
print(dct2)
print("")

dct3 = {}
for char in str:
    if char in dct3:
        dct3[char] += 1
    else:
        dct3[char] = 1
print(dct3)
print("")

dct4 = {}
for char in str:
    dct4[char] = dct4.get(char, 0) + 1

print(dct4)
print("")