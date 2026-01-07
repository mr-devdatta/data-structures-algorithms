
class naturalNumbers:    
    
    @staticmethod
    def sum(number):
        if number < 1:
            print("Invalid number")
        elif number == 1:
            print("The Number is 1")
        else:
            sum = 0
            for i in range(1, number + 1):
                sum += i
            print(sum)
    

naturalNumbers.sum(10)
