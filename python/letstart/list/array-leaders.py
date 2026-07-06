# Input: arr = [16, 17, 4, 3, 5, 2]
# Output: [17, 5, 2]
# Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.

# Input: arr = [10, 4, 2, 4, 1]
# Output: [10, 4, 4, 1]
# Explanation: Note that both of the 4s are in output, as to be a leader an equal element is also allowed on the right. side

# Input: arr = [5, 10, 20, 40]
# Output: [40]
# Explanation: When an array is sorted in increasing order, only the rightmost element is leader.

# Input: arr = [30, 10, 10, 5]
# Output: [30, 10, 10, 5]
# Explanation: When an array is sorted in non-increasing order, all elements are leaders.

lst =  [30, 10, 10, 5]

final = []
for i, v in enumerate(lst):
    if all(val > v  for val in lst[i+1:]):
        final.append(v)
print(final)
