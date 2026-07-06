car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car["name"] = "Nexton"

for tpl in car.items():
    print(tpl)

print(" ------------------- ")

ky =  car.keys()
print(ky)

print(" ------------------- ")

# car.pop("year")
del car["year"]

for tpl in car.items():
    print(tpl)

print(" ------------------- ") 

val = car.values()
print(val)