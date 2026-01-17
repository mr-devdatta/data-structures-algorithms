
str = "aaabbccaaaa"
# output : ['a', 'b', 'c', 'a']


output = ""
lastChar = ""
for char in str:
    if char != lastChar:
        output += char
    lastChar = char

print(list(output))


dct = {}
lastChar = ""
for char in str:
    if char == lastChar:
        dct[char] = dct.get(char) + lastChar
    else:
        dct[char] = char    
    lastChar = char
print(dct)
print(list(dct.keys()))
print(list(dct.values()))
print(list(dct.items()))


