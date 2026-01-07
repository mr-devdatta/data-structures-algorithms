

class digits:

    @classmethod
    def sum(cls, number):
        n = number
        sumOfDigit = 0

        while n > 0:
            print(f"{n}, ", end="")
            lastDigit = int(n % 10)
            n = int(n / 10)
            sumOfDigit += lastDigit
            print(f"{n}, {lastDigit}")
        
        print(f"Final Sum {sumOfDigit}")

digits.sum(5678)