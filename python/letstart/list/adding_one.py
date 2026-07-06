# Input: arr[] = [5, 6, 7, 8]
# Output: [5, 6, 7, 9]
# Explanation: 5678 + 1 = 5679

# Input: arr[] = [9, 9, 9]
# Output: [1, 0, 0, 0]
# Explanation: 999 + 1 = 1000

lst = [9, 9, 9]
strDigit = "".join(str(i) for i in lst)
print(int(strDigit) + 1)


