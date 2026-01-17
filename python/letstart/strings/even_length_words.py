txt = "This is gopal that is girl mother father sister"
lst = txt.split() # default is space
#print(lst)

n = ""
for wrd in lst:
    if len(wrd) % 2 == 0:
        n += " " + wrd

n = n.strip()
print(n)

lis2 = [wrd for wrd in lst if len(wrd) % 2 == 0]
print(" ".join(lis2))

xxx = "devdatta"
length = len(xxx)
mid = length // 2
s = xxx[:mid].upper() + xxx[mid:]
print(s)
