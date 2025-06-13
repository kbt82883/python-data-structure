# 인접한 정점과 가중치
Graph = {
    "A": [("B", 29), ("F", 10)],
    "B": [("A", 29), ("C", 16), ("G", 15)],
    "C": [("B", 16), ("D", 12)],
    "D": [("C", 12), ("E", 22), ("G", 18)],
    "E": [("D", 22), ("F", 27), ("G", 25)],
    "F": [("A", 10), ("E", 27)],
    "G": [("B", 15), ("D", 18), ("E", 25)],
}


def weightSum():
    sum = 0

    for v in Graph:
        for e in Graph[v]:
            sum += e[1]

    return sum


def display():
    for v in Graph:
        for e in Graph[v]:
            if v < e[0]:  # AB는 출력 BA처럼 거꾸로는 출력x
                print("[%s%s %d] " % (v, e[0], e[1]), end="")
        print()


if __name__ == "__main__":
    print("weight Value :", weightSum())
    display()
