
A = "Geeks for Geeks".lower()
B = "Learning from Geeks for Geeks".lower()

Alst  = A.split()
Blst = B.split()

print(Alst)
print(Blst)

arr = []
for i in Blst:
    if i not in Alst:
        arr.append(i)
print(arr)



ASet = set(Alst)
BSet = set(Blst)

print(ASet)
print(BSet)

CSetList = list(BSet - ASet)
print(CSetList)

# ---------------------

Str = A + " " + B
print(Str)
Words = Str.split()
print(Words)

dct = {}
for wrd in Words:
    dct[wrd] = dct.get(wrd, 0 ) + 1
print(dct)

uncommon = [ wrd for wrd in dct if dct[wrd] == 1  ]
print(uncommon)