s = "hello world hello everyone"

lst  = s.split()

dct = {}
for wrd in lst:
    dct[wrd] = dct.get(wrd, 0) + 1

print(dct)