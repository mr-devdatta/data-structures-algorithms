
words = ["abb", "bba", "abc", "cba", "aabbcc", "xyz", "zyx", "xxyyzz"]

# output : [['abb', 'bba'], ['abc', 'cba', 'aabbcc'], ['xyz', 'zyx', 'xxyyzz']]

dct = {}


def uniqChars(wrd):
    uniq = []
    for ch in wrd:
        if ch not in uniq:
            uniq.append(ch)
    
    #print(uniq)
    return uniq


for wrd in words:
    #key = "".join(sorted(set(wrd)))     # use set()
    key = "".join(sorted(uniqChars(wrd)))

    if key in dct:
        #dct[key] = dct.get(key) + [wrd]
        dct[key].append(wrd)
    else:
        dct[key] = [wrd]
        
#print(dct)
print(list(dct.values()))