
lst = [5, [2, 3, 4], [7, 8], 1]
print(f"Original List => {lst}")
print(type(lst))

finalList = []
for i in lst:
    if isinstance(i, list):
        finalList.extend(i)
    else:
        finalList.append(i) 


print(f"Finale List => {finalList}")

finalList.sort()
print(f"Order List  => {finalList}")

finalList.reverse()
print(f"Finale List => {finalList}")

