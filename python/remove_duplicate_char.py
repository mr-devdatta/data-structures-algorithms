text  = "this is gopal that is girl mother father sister"

print("".join(set(text))) # order changed
# OR 
print("".join(dict.fromkeys(text))) # order preserved
# or

result = ''
for char in text:
    if char not in result:  # and char != " "
        result += char
print(result)

# unique_chars = [char for char in dict.fromkeys(text) if char != " "]
# unique_no_space = "".join(dict.fromkeys(text.replace(" ", "")))