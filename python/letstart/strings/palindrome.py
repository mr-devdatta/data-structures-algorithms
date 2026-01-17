# Key Difference: Symmetrical vs. Palindrome
    # Symmetrical: The halves are identical ("abcabc").
    # Palindrome: The word reads the same backward and forward ("abccba").
# ---------------------------------------------------------------------------------

str = "ABCDEFGHIJqJIHGFEDCBA"   # radar , level, 
print(f"{str} => {len(str)} chars")

# ---------------------------------------------------------------------------------
if str == str[::-1]:
    print("palindrome")
else:
    print("Not a palindrome")
# ---------------------------------------------------------------------------------

length = len(str)
half = length // 2

first_half = str[:half]             # Step 1: Slice the first half

# Step 2: Determine where the second half starts
if length % 2 == 0:  
    second_half = str[half:]        # If even, start exactly at the midpoint
else:   
    second_half = str[half+1:]      # If odd, skip the middle character (half + 1)

if first_half == second_half:
    print("palindrome")
else:
    print("Not a palindrome")
# ---------------------------------------------------------------------------------

#using 2 pointer
palindromeFlag = True
leftPointer = 0
rightPointer = len(str) - 1

while leftPointer < rightPointer:
    if str[leftPointer] != str[rightPointer]:
        palindromeFlag = False
        break
    leftPointer += 1
    rightPointer -=1
if palindromeFlag:
    print("palindrome using 2 pointer")
else:
    print("Not a palindrome using 2 pointer")
# ---------------------------------------------------------------------------------

palindromeFlag = True
mid = len(str) // 2

for i in range(mid):
    if len(str) % 2 == 0:
        if str[i] != str[mid + i]:
            palindromeFlag = False
            break
    else:
        if str[i] != str[mid + i + 1]:
            palindromeFlag = False
            break

if palindromeFlag:
    print("palindrome using")
else:
    print("Not a palindrome using")

