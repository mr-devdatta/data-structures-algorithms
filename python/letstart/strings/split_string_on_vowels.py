str = 'GFGaBSTuGFGiBSTuGFGoBST'

vowels = "aeiouAEIOU"
print(vowels)

pos = 0
substr = ""
lst1 = []
for ch in str:
    if ch in vowels:
        lst1.append(substr)
        substr = ""
    else:
        substr += ch
print(lst1)