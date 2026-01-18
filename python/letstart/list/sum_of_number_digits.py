
lst = [123, 456, 789, 456456]
print(lst)

finalLst = []
for i in lst:
    finalLst.append(sum(int(digit) for digit in str(i)))

print(finalLst)

res = [ sum(int(digit) for digit in str(i)) for i in lst  ]
print(res)
