
class multificationTable:

    def __init__(self, upto = 10):
        self.upto = upto

    def showTable(self, number):
        for i in range(1, self.upto + 1):
            print(f"{number} * {i} = {number * i}")
        

obj = multificationTable(12)
obj.showTable(7.1)