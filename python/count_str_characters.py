
str = "devdatta khadakban"
str = str.replace(" ", "").casefold()
print(str)

#  SOLUTION 1  ----------------------------------------------------------------------------

lst = list(str)
print(lst)

d = {}
for i in lst:    
    if i in d:
        d[i] += 1 
    else:
        d[i] = 1 
print(d)

#  SOLUTION 2  ----------------------------------------------------------------------------

dct = {}
for char in str:
    dct[char] = dct.get(char, 0) + 1
    
print(dct)

