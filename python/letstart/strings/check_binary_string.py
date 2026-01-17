s = "101010000111"

ss = set(s)
print(ss)

flag = True
for char in ss:
    if char not in '10':  # or [ '1', '0' ] => do not use [1 , 0]  it will compare string with integer
        flag = False
        print("not binary string")
        break
if flag:
    print("BINARY STRING")
# -----------------------------------------

bset =set('10')
print(bset)
if set(s).issubset(bset):
    print("BINARY STRING")
else:
    print("not binary string")