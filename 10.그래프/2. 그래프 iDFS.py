vName = ["A", "B", "C", "D", "E", "F", "G", "H"]
visited = [False] * len(vName)  # 방문기록


Graph = [
    [1, 2],
    [0, 3],
    [0, 3, 4],
    [1, 2, 5],
    [2, 6, 7],
    [3],
    [4, 7],
    [4, 6],
]

from queue import LifoQueue  # 내장 스택 사용


class Stack(LifoQueue):
    def peek(self):
        if not self.empty():
            return self.queue[-1]
        raise Exception("Empty")


# 깊이우선탐색 반복문
def iDFS(s):
    S = Stack()

    S.put(s)
    visited[s] = True
    print("[%c] " % vName[s], end="")

    while not S.empty():
        s = S.peek()
        flag = False

        for t in Graph[s]:  # 인접정점 t
            if visited[t] == False:  # 방문한 적이 없으면
                S.put(t)
                visited[t] = True
                print("[%c] " % vName[t], end="")

                flag = True
                break

        if flag == False:  # 아무 정점도 방문하지 않았으면 스택에서 pop
            S.get()


if __name__ == "__main__":
    print("iDFS : ", end="")
    iDFS(1)
