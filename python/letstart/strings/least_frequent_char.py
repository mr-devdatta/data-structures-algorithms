
str = "GeeksforGeeks"
dct = {}
for char in str:
    if char in dct:
        dct[char] += 1
    else:
        dct[char] = 1    
print(dct)
leastChar1 = min(dct, key=dct.get)
print(leastChar1)

dct2 = {}
for ch in str:
    dct2[ch] = dct.get(ch, 0) + 1

print(dct2)
leastChar2 = min(dct2, key=dct2.get)
print(leastChar2)