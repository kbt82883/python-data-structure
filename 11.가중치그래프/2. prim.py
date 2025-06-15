# O(n^2)

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

vCnt = len(Graph)
INF = 1000  # 임의의 큰 값 infinite
dist = [INF] * vCnt  # distance
visited = [False] * vCnt


def findMin():
    minDist = INF  # 일단 아무 값이나
    minV = 0  # 최소 정점 인덱스

    for v in range(vCnt):
        if visited[v] == False and dist[v] < minDist:
            minDist = dist[v]
            minV = v

    return minV


def prim(vName):  # 시작 정점
    dist[ord(vName) - 65] = 0  # 문자를 아스키코드로 변환 (65는 대문자 A)

    for i in range(vCnt):

        for j in range(vCnt):
            if dist[j] == INF:
                print("  * ", end="")
            else:
                print("%3d " % dist[j], end="")
        print()

        vNum = findMin()
        vName = chr(vNum + 65)  # 다시 문자로

        visited[vNum] = True
        # print("[%c(%d)] " % (vName, dist[vNum]), end="")

        for e in Graph[vName]:  # 시작정점의 인접 정점들
            vNum = ord(e[0]) - 65
            if visited[vNum] == False and e[1] < dist[vNum]:
                dist[vNum] = e[1]


if __name__ == "__main__":
    prim("G")
