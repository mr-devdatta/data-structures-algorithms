
string = "Geeks$For$Ge^)eks"

sp = ""
spUniq = set()
for char in string:
    if not char.isalnum():
        sp += char
        spUniq.add(char)
    
print(sp)
print("".join(spUniq))