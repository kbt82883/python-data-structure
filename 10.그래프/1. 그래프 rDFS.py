# O(n^2)
vName = ["A", "B", "C", "D", "E", "F", "G", "H"]
visited = [False] * len(vName)  # 방문기록


Graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],  # 시작정점 s의 인접정점 t=1
    [1, 0, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0],
]


# 깊이우선탐색 순환호출
def rDFS(s):  # 시작정점 s
    visited[s] = True
    print("[%c] " % vName[s], end="")

    for t in range(len(vName)):  # 인접정점 t
        if Graph[s][t] == 1 and visited[t] == False:  # 방문하지 않은
            rDFS(t)


if __name__ == "__main__":
    print("rDFS : ", end="")
    rDFS(1)
