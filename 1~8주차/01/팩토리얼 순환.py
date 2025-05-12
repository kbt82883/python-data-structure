def iFact(n):
    result = 1
    for i in range(n, 0, -1):
        result = result * i
    return result

def rFact(n):
        if n ==1:
            return 1
        else:
            return n* rFact(n-1)

print(iFact(5)) #반복
print(rFact(5)) #순환