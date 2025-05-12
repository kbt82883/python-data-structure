from CircularQueue import CircularQueue

class CircularDeque(CircularQueue):  # 서큘러큐 상속
    
    def __init__(self, capacity = 10):
        super().__init__(capacity)  # 부모 생성자 필수

    def addRear(self, e):  # enqueue
        self.enqueue(e)

    def addFront(self,e):
        if not self.isFull():
            self.array[self.front] = e
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else:
            print("Overflow")

    def deleteFront(self):  # dequeue
        self.dequeue()

    def deleteRear(self):
        if not self.isEmpty():
            e = self.array[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return e
        else:
            print("Underflow")

    def getFront(self):  # peek
        self.peek()

    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        else:
            print("Underflow")

if __name__=="__main__":
    import random

    DQ = CircularDeque()
    for _ in range(4):
        DQ.addFront(random.randint(65, 90))
    DQ.display()

    for _ in range(4):
        DQ.addRear(random.randint(65, 90))
    DQ.display()

    for _ in range(3):
        print("[%c]" % DQ.deleteRear(), end=" ")
    print()
    DQ.display()

    for _ in range(2):
        print("[%s]" % DQ.deleteFront(), end=" ")
    print()
    DQ.display()
    