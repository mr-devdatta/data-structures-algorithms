str = "devdattageeksforgeeusfdfikso"

vowels = set("aeiou")
strSet = set(str.lower())

print(vowels)
print(strSet)

if vowels.issubset(strSet):
    print("String contain all vowels")
else:
    print("String doesn't contain all vowels")

# -------------------------------------------------------------------------------------------------------------

vow = "aeiou"
if all(char in str for char in vow):
    print("String contain all vowels")
else:
    print("String doesn't contain all vowels")
