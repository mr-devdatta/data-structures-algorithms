#Input   :   words = ["eat", "tea", "tan", "ate", "nat", "bat"]
#Output  :   [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

dct = {}
# for wrd in words:
#     wrdkey = "".join(sorted(wrd))

#     if wrdkey in dct:
#         dct[wrdkey] = dct.get(wrdkey) + [wrd]
#     else:
#         dct[wrdkey] = [wrd]
     
# lstFinal = []
# for lst in dct.values():
#     lstFinal.append(lst)

# print(dct)
# print(lstFinal)

for wrd in words:
    dctKey = "".join(sorted(wrd))

    if dctKey in dct:
        dct[dctKey].append(wrd)
    else:
        dct[dctKey] = [wrd]
       
print(dct)
print(list(dct.values()))
