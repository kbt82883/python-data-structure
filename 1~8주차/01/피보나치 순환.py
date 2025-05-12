count = 0

def rFib(n):  # 안좋음
    global count
    count += 1

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rFib(n-2) + rFib(n-1)
    
def iFib(n):
    a = 0
    b = 1
    print("Fibonaccci : 0, 1", end='')

    for _ in range(2, n+1):
        a,b = b, a+b
        print(',',b,end='')

    print(' ')
    return b

print('rFib : %d - count : %d' % (rFib(10), count))
print(iFib(10))