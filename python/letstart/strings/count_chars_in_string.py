
str = 'geekforgeeks is best for geeks'
str = str.replace(" ", "")
print(str)
uniqChars = set(str)
print(uniqChars)

dct = {}
for char in uniqChars:
    dct[char] = str.count(char)
print(dct)


print(str)
dct2 = {}
for ch in str:
    if ch in dct2:
        dct2[ch] += 1
    else:
        dct2[ch] = 1
print(dct2)

