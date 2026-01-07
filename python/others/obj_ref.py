
a = [1] * 5
#print(a)

b = [[2]] * 5  
print(b)
# output : [[2], [2], [2], [2], [2]]
# This will not create five independent list of [2], instead, 
# it creates one list object [2] and then creates five references that all point to that same exact object in memory.
# Think of it like five people all holding a string attached to the same balloon.

b[2].append(9)
print(b)
# OUTPUT : [[2, 9], [2, 9], [2, 9], [2, 9], [2, 9]]
# You are telling Python: "Go to the object at index 2 and add 9 to it."
# Since all five indices (0, 1, 2, 3, and 4) point to the same memory object, 
# when you pop it or change its value, it looks changed to everyone holding a adress.
# Because b[0], b[1], b[2], b[3], and b[4] all look at the same memory address, they all show [2, 9].


# How to do it correctly

# This creates 5 separate list objects
b = [[2] for _ in range(5)]
b[2].append(9)
print(b)
# Output: [[2], [2], [2, 9], [2], [2]]
