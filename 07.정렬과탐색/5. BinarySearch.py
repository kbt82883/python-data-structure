import random

def seqSearch(A, key):  # 순차 탐색
    n = len(A)

    for i in range(n):
        if A[i] == key:
            return i
        
    return -1

def insertionSort(A):  # 삽입정렬
    n = len(A)

    for i in range(1, n):
        key = A[i]
        j = i - 1

        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1

        A[j+1] = key

def iBinarySearch(A, key):  # 반복문 이진탐색
    low = 0
    high = len(A) - 1

    while(low <= high):
        mid = (low + high) // 2  # 정수나누기
        print(A[mid], end=' ')

        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1

def rBinarySearch(A, key, low, high):  # 순환호출 이진탐색
    if low <= high:
        mid = (low + high) // 2  # 정수나누기
        print(A[mid], end=' ')

        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return rBinarySearch(A, key, low, mid - 1)
        else:
            return rBinarySearch(A, key, mid + 1, high)

    return -1

if __name__=="__main__":
    A = []
    for i in range(15):
        A.append(random.randint(1, 100))

    insertionSort(A)

    print("A[] =", A)

    key = int(input("Input Search Key : "))
    # idx = seqSearch(A, key)
    # idx = iBinarySearch(A, key)
    idx = rBinarySearch(A, key, 0, 14)

    print()
    if idx != -1:
        print("Find at pos %d." % idx)
    else:
        print("No key to Find.")