class student:

    school_name = "BHB"

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

    def updateSchool(cls, name):
        cls.school_name = name


obj1 = student("Dev")
obj2 = student("Ni3")

student.school_name = "Gurucool"
obj1.show()
obj2.show()


#obj1.updateSchool("SADSDSS")
print(obj1.school_name)

print(obj2.school_name)