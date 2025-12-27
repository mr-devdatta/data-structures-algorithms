
def printIncreasingPower(x):    
    i = 1
    while(i <= x):
        val = i**2
        i += 1
        if val <= x :
            print(val, end=" ")
        else:
            break 

def printIncreasingPower1(x):    
    i = 1
    for i in range(2, x, i*i):
        print(i*i)


printIncreasingPower1(10)

