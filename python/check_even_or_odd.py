
class checkNumber:

    def checkEvenOrOdd(self, number):
        if number % 2 == 0:
            print(f"The number {number} is even nuber")
        else:
            print(f"The number {number} is ODD nuber")

obj = checkNumber()
obj.checkEvenOrOdd(2345)