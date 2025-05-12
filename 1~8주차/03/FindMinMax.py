import random

def find_min_max(A):
    
    min = max = A[0]

    for i in range(1,len(A)):
        if min > A[i]:
            min = A[i]
        if max < A[i]:
            max = A[i]
    
    return min, max

A = []
for _ in range(10):
    A.append(random.randint(1,10))

if __name__ == '__main__':
    print(A)
    print(find_min_max(A))
