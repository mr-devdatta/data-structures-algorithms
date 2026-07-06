
lst = [3, 6, 12, 2, 56, 6, 23, 99, 72, 1, 103, -5, 87]

min = float("inf")
max = -1 

for i in lst:
    if i < min:
        min = i

    if i > max:
        max = i

print(min, max)

