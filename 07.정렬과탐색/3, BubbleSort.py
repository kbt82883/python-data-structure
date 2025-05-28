def printStep(A, idx):
    print("   Step %d : " % idx, end="")
    print(A)


def insertionSort(A):
    n = len(A)

    for i in range(1, n):
        key = A[i]  # 오른손에 카드 한장
        j = i - 1

        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1

        A[j + 1] = key

        printStep(A, i)


def bubbleSort(A):
    n = len(A)

    for i in range(n - 1):
        flag = False
        for j in range(1, n - i):
            if A[j - 1] > A[j]:
                A[j - 1], A[j] = A[j], A[j - 1]
                flag = True

        if not flag:
            break

        printStep(A, i + 1)


if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]

    L = list(data)
    print("Before    :", L)
    bubbleSort(L)
    print("Bubble    :", L)
    print()
