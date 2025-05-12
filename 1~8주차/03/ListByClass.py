class ArrayList:
    def __init__(self, capacity = 100):
        self.capacity = capacity  # 용량
        self.size = 0
        self.array = [None] * capacity

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def insert(self,pos,e):  # 포지션, 엘리먼트
        if not self.isFull() and 0 <= pos <= self.size:  # 사이즈보다 몇칸 띄어서 삽입하면 안됨
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i-1]  # 오른쪽으로 하나씩 밀기
            self.array[pos] = e
            self.size += 1  # 사이즈 늘음
        else:
            print("Overflow or Invalid Position.")

    def delete(self,pos):
        if not self.isEmpty() and 0 <= pos < self.size:  # 사이즈보다 몇칸 띄어서 삽입하면 안됨
            e = self.array[pos]
            for i in range(pos, self.size-1):  # 왼쪽으로 하나씩 덮어쓰기
                self.array[i] = self.array[i+1]
            self.size -= 1  # 사이즈 줄음
            return e
        else:
            print("Underflow or Invalid Position.")

    def getEntry(self, pos):
        if 0 <= pos < self.size:  #배열 사이즈 안의 pos이면
            return self.array[pos]
        else:
            return None
        
    def findElement(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return i
        return -1
        
    def __str__(self):
        return str(self.array[0:self.size])

if __name__ == "__main__":
    L = ArrayList(50)

    L.insert(0,"A")
    L.insert(1,"B")
    L.insert(1,"C")
    print(L)

    L.insert(4,"D")
    L.insert(3,"E")
    print(L)

    e = input('Input Element to delete : ')
    idx = L.findElement(e)

    if idx != -1:
        print("[%c] is deleted." % L.delete(idx))
    print(L)    