
def fact1(n):
    rs = 1
    if n > 0:
        for i in range(1, n+1):
            rs = rs * i
        print(rs)
        
def fact(n):
    if n == 1 or n == 0:
        return 1 
    else:
        return n * fact(n-1)
        
        
print(fact(5))

