#	Check if two strings are rotations ->  "ABCD", "CDAB" → true.

str1 = "ABCD"
str2 = "CDAB"

def abc(str1, str2):
    if len(str1) != len(str2):
        return False
    
    temp = str1 + str1
    print(temp)

    return str2 in temp

print(abc(str1, str2))