N = 20

class MaxHeap:
    def __init__(self):
        self.heap = [None] * N
        self.heapSize = 0

    def upHeap(self):
        i = self.heapSize
        key = self.heap[i]

        while i != 1 and key > self.heap[i // 2]:  # 내가 부모가 있는지? 부모보다 큰지?
            self.heap[i] = self.heap[i // 2]  # 부모의 키 값을 아래로 내리고
            i = i // 2  # 내 위치는 부모 자리로

        self.heap[i] = key  # 반복문 끝나고 화살표 가리키는 곳에 나의 키 값

    def insertItem(self, item):
        self.heapSize += 1
        self.heap[self.heapSize] = item
        self.upHeap()

    def downHeap(self):
        key = self.heap[1]  # 루트 노드가 나
        p = 1  # parents
        c = 2  # child, 왼쪽 자식 노드임

        while c <= self.heapSize:  # 존재하는 자식 노드라면
            if c < self.heapSize and self.heap[c+1] > self.heap[c]:  # 오른쪽 노드가 왼쪽 노드보다 값이 크면
                c += 1  # 나와 비교할 자식 노드는 오른쪽 노드임
            
            if key >= self.heap[c]:  # 나와 (오른쪽 왼쪽 중 더 큰) 자식 노드를 비교
                break

            self.heap[p] = self.heap[c]  # 부모 노드 값에 자식 노드 값을 넣고
            p = c  # 화살표가 자식으로 내려감
            c *= 2  # 자식도 바뀐 부모에 따라 바뀜

        self.heap[p] = key  # 반복문 끝나서 최종 화살표가 가리키고 있는 곳에 key값을 넣음


    def deleteItem(self):
        key = self.heap[1]

        self.heap[1] = self.heap[self.heapSize]  # 맨 마지막 노드를 루트노드로 덮어 씌움
        self.heapSize -= 1  # 사이즈를 줄이면서 마지막 노드 삭제
        self.downHeap()

        return key


if __name__ == "__main__":
    H = MaxHeap()

    data = [9,7,6,5,4,3,2,2,1,3]

    for d in data:
        H.insertItem(d)
        print("Heap :", H.heap[1:H.heapSize + 1])

    print("-------------------------------------")
    H.insertItem(8)
    print("Heap :", H.heap[1:H.heapSize + 1])
    print("-------------------------------------")

    print("[%d] is deleted." % H.deleteItem())
    print("Heap :", H.heap[1:H.heapSize + 1])