# 1.	Reverse each word without reversing order
#       "I love PHP" → "I evol PHP" (No strrev())
str = "  I love php and Python programming" 
print(str)

def reverse_string(str):
    str_2_List = str.split()

    new_list = [word[::-1] for word in str_2_List]

    rev_Str = " ".join(new_list)
    return rev_Str

print(reverse_string(str))
