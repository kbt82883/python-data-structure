def iPower(x,n):
    result = 1

    for _ in range(n):
        result *= x
    
    return result

def rPower(x,n):
    if n == 0:
        return 1
    elif n%2 == 0:
        return rPower(x*x, n//2)
    else:
        return x * rPower(x*x, (n-1)//2)
    
print(iPower(2,10))
print(rPower(2,10))