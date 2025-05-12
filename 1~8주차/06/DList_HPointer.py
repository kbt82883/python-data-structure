# 이중연결리스트의 헤드 포인터 버전
# deleteFirst, deleteLast는 여러분이 하시기 바랍니다 (시험인가)

class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev  # 이전 노드도 받음
        self.next = next

class DListType:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    # def isFull 은 없음, 용량이 없어서

    def insertFirst(self, data):  # addFront, addRear로 바꾸면 덱이 됨
        node = Node(data, next = self.head)

        if self.isEmpty():
            self.head = self.tail = node
        else:
            self.head.prev = node
            self.head = node

        self.size += 1

    def insertLast(self, data):
        node = Node(data, prev = self.tail)

        if self.isEmpty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def deleteFirst(self):
        if self.isEmpty():
            print("Underflow")
            return
        
        p = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = p.next
            p.next.prev = None
        
        self.size -= 1

        return p.data
    
    def deleteLast(self):
        if self.isEmpty():
            print("Underflow")
            return
        
        p = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = p.prev
            p.prev.next = None

        self.size -= 1

        return p.data

    def printList(self):  # 단순연결리스트와 같음
        p = self.head

        while True:
            print("[%s] <-> " % p.data, end="")
            if p == self.tail:
                break
            p = p.next
        print("\b\b\b\b    ")

    # def printList(self):
    #     p = self.head
    #     while p is not None:
    #         print("[%s] <-> " % p.data, end="")
    #         p = p.next
    #     print("\b\b\b\b    ")  # 마지막 <-> 없애기 위한 처리


if __name__=="__main__":
    DL = DListType()

    DL.insertLast("C"); DL.printList()
    DL.insertFirst("A"); DL.printList()
    DL.insertFirst("B"); DL.printList()
