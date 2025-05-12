from ArrayStack import ArrayStack

S = ArrayStack()

str = input('InputString : ')
for c in str:
    S.push(c)

print('Print String : ', end='')
while not S.isEmpty():
    print(S.pop(), end='')
print()