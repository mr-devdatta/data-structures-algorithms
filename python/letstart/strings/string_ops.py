#Input - ['chb', 'xyz', 'bch', 'abc', 'hbc', 'cba']
#Output - ['chb', 'bch', 'hbc', 'xyz', 'abc', 'cba']

lst = ['chb', 'xyz', 'bch', 'abc', 'hbc', 'cba']
print(lst)

dct = {}

for wrd in lst:
    wrdLst = list(wrd)
    wrdLst.sort()
    wrdIndex = "".join(wrdLst)
    #print(f"{wrdIndex} => {wrd}")

    if wrdIndex in dct:
        dct[wrdIndex] += [wrd]
    else:
        dct[wrdIndex] = [wrd]
        pass

#print(dct)

final = []
for subList in dct.values():
    final.extend(subList)
print(final) 
# -------------------------------------------------------------------------

groups = {}
for word in lst:
    key = ''.join(sorted(word))   # create anagram key

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

final = []
for group in groups.values():
    final += group   # or final.extend(group)

print(final)