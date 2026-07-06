# from copy import deepcopy

# lst = [10, 20, 4, 45, 99]

# l2 = deepcopy(lst)


# lst.sort()
# print(lst)
# print(lst[-2])

# l3 = sorted(l2)
# print(l3)
# print(l3[-2])
# # -------------------------




nums = [10, 5, 20, 8, 15]

first_Large = float('-inf')  # consider -1, i.e -inf
second_Large = float('-inf')   # consider -1, i.e -inf


for n in nums:
    if n > first_Large:
        second_Large = first_Large  # -1, first iterator
        first_Large = n
    elif n != first_Large and n > second_Large:   # 2nd iterator
        second_Large = n

print(second_Large)