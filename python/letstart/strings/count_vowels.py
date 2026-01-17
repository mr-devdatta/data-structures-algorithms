str = "Python is Funnnnnnnn!"

str = str.replace(" ", "").lower()
strSet = set(str)

#print(strSet)

vowels  = "aeiou"
vowelList = list(vowels)
#print(vowelList)

final = []
for char in strSet:
    if char in vowelList:
        final.append(char)

#print(final)
# -------------------------

str1 = "Python is Funii!"
v = "aeiouAEIOU"

vSet = list(set([ char for char in str1 if char in v ]))
print(vSet)

