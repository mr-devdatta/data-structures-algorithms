

d = {'gfg' : [5,6,7,8],' is' : [10,11,7,5], 'best' : [6,12,10,8], 'for' : [1,2,5]}

l2 = []
for l1 in d.values():
    l2.extend(l1)

 
l3 = [  k for k in d.values()  ] 
print(sum(l3, []))

print(l2)
print(list(set(l2)))