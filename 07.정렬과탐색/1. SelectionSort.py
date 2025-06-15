# O(n^2)


def printStep(A, idx):
    print("   Step %d : " % idx, end="")
    print(A)


def selectionSort(A):
    n = len(A)

    for i in range(n - 1):
        minI = i
        for j in range(i + 1, n):
            if A[j] < A[minI]:
                minI = j
        A[i], A[minI] = A[minI], A[i]
        printStep(A, i + 1)


if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]

    L = list(data)
    print("Before    :", L)
    selectionSort(L)
    print("Selection :", L)
