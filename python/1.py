class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def marks(self):
        print(self.__salary)

    @marks.setter
    def marks(self, salary):
        self.__salary = salary
        print(self.__salary)


e = Employee(50000)
e.marks
e.marks = 123423