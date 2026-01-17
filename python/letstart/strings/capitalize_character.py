txt = "this is gopal that is girl mother father sister"
lst = txt.split()

nwLst=[]
for wrd in lst:
    s1 = wrd[0].upper() + wrd[1:-1] + wrd[-1].upper()
    nwLst.append(s1)

print(" ".join(nwLst))


ls = " ".join([
    wrd[0].upper() + wrd[1:-1] + wrd[-1].upper()
    for wrd in lst
])
print(ls)