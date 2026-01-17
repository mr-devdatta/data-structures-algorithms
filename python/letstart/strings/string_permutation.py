import itertools

s = "123"
li = [''.join(p) for p in itertools.permutations(s)]
print(li)

length = len(s)

for i in range(0, length):
    
    for j in range(j+i, length):
        
    