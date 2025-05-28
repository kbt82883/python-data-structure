class SortedArraySet:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

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
        if self.contains(e) or self.isFull():
            return
        
        self.array[self.size] = e
        self.size += 1

        for i in range(self.size - 1, 0, -1):
            if self.array[i-1] < self.array[i]:
                break
            self.array[i-1], self.array[i] = self.array[i], self.array[i-1]

    def delete(self, e):
        if not self.contains(e):
            return
        
        i = 0
        while self.array[i] < e:
            i += 1
        
        self.size -= 1

        while i < self.size:
            self.array[i] = self.array[i + 1]
            i += 1

    def union(self, setB):
        setC = SortedArraySet()  # 결과 집합
        i = 0
        j = 0

        while i < self.size and j < setB.size:
            a = self.array[i]
            b = setB.array[j]
            
            if a == b:
                setC.append(a)
                i += 1
                j += 1
            elif a < b:
                setC.append(a)
                i += 1
            else:
                setC.append(b)
                j += 1

        while i < self.size:
            setC.append(self.array[i])
            i += 1

        while j < setB.size:
            setC.append(setB.array[j])
            j += 1

        return setC

if __name__ == "__main__":
    import random
    setA = SortedArraySet()
    for i in range(5):
        setA.insert(random.randint(1,9))

    print('Set A : ', setA)
