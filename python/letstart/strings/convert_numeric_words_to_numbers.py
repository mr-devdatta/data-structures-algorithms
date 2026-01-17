
dct  = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", 
      "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

str = "one zero four zero one"


lst = "".join([dct[word] for word in str.split() if word in dct])
print(lst)

