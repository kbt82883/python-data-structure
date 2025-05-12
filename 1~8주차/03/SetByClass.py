class ArraySet:
    def __init__(self, capacity = 100):
        self.capacity = capacity  # 용량
        self.size = 0
        self.array = [None] * capacity

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity
    
    def __str__(self):
            return str(self.array[0:self.size])
    
    def contains(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return True
            
        return False
    
    def insert(self, e):
        if not self.contains(e) and not self.isFull():  # 이미 중복 엘리먼트가 없고 꽉 차있지 않으면
            self.array[self.size] = e
            self.size += 1

    def delete(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                self.array[i] = self.array[self.size-1]  # 제일 뒤에 있는 요소로 채움 (이동 연산이 덜하기 위해서)
                self.size -= 1
                return
            
    def union(self, setB):  # 합집합
        setC = ArraySet()
        
        for i in range(self.size):
            setC.insert(self.array[i])
        for i in range(setB.size):
            if not setC.contains(setB.array[i]):  # 없는 애만 찾아서
                setC.insert(setB.array[i])  # 넣기

        return setC
    
    def intersect(self, setB):  # 교집합
        setC = ArraySet()

        for i in range(self.size):
            if setB.contains(self.array[i]):
                setC.insert(self.array[i])
        
        return setC

    def difference(self, setB):  # 차집합
        setC = ArraySet()

        for i in range(self.size):
            if not setB.contains(self.array[i]):
                setC.insert(self.array[i])

        return setC


if __name__ == "__main__":
    S = ArraySet()
    S.insert(10)
    S.insert(30)
    S.insert(40)
    S.insert(50)

    T = ArraySet()
    T.insert(40)
    T.insert(60)
    T.insert(20)
    T.insert(50)

    print('S =', S)
    print('T =', T)

    print('S U T =', S.union(T))
    print('S ^ T =', S.intersect(T))
    print('S - T =', S.difference(T))