txt = "This is gopal that is girl mother father sister"
lst = txt.split() # default is space
print(lst)

revrseLst = lst[::-1]
print(revrseLst)

rStr = " ".join(revrseLst)
print(rStr)
# ------------------------------------------

print(' '.join(txt.split()[::-1]))

# ------------------------------------------

wordLst = txt.split()

rStr= ""
for i in wordLst:
    rStr = i + " " + rStr

rStr = rStr.strip()

print(rStr)