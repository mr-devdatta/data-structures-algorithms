
s = "geeksfor geeks"

lst = ''.join(list(set(s)))
#print(lst)
# --------------------------------------------------------------------

dct = dict.fromkeys(s)
uniq = "".join(dct)
#print(dct)

# --------------------------------------------------------------------

st = set()

for char in s:
    if char != " ":
        st.add(char)
print(st)
print("".join(st))