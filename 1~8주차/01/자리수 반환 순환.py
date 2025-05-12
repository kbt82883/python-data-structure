#교수님 답
def rPrint(n):
    if n < 10:
        print(n%10)
        return "end"
    else:
        print(n%10)
        return rPrint(n//10)

def f(n):
    if n == 0:
        return "end"
    else:
        print(n%10)
        return f(n//10)

print(rPrint(3728))
print(f(3728))