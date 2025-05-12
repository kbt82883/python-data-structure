class Node:  # 학생 노드
    def __init__(self, data, next = None):  # 데이터와 뒷 노드, next초기값도 필요없긴함함
        self.data = data
        self.next = next

class ListType:
    def __init__(self):
        # 헤드포인터 = 제일 첫 학생을 가르킴
        self.tail = None  # 선생 노드, 아직 아무도 없음
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    # def isFull 은 없음, 용량이 없어서

    def insertFirst(self, data):  #덱의 insertFront()
        node = Node(data)
        
        if self.isEmpty():  # 노드가 없으면
            node.next = node  # 내가 날 가리켜
            self.tail = node  # tail이 날 가리켜
        else:  # 노드가 하나 이상
            node.next = self.tail.next  # 첫번쨰 노드 가리켜
            self.tail.next = node
            # self.tail = node  # 이거만 지우면 insertFirst

        self.size += 1

    def insertLast(self, data):  #덱의 insertRear()
        node = Node(data)
        
        if self.isEmpty():  # 노드가 없으면
            node.next = node  # 내가 날 가리켜
            self.tail = node  # tail이 날 가리켜
        else:  # 노드가 하나 이상
            node.next = self.tail.next  # 첫번쨰 노드 가리켜켜
            self.tail.next = node
            self.tail = node

        self.size += 1

    def deleteFirst(self):  # 덱의 deleteFront()
        if not self.isEmpty():
            p = self.tail
            q = p.next

            if p == q:
                self.tail = None
            else:
                p.next = q.next

            self.size -= 1
            return q.data  # 삭제된 데이터

        else:
            print("Underflow")

    def deleteLast(self):  # 덱의 deleteRear()
        if not self.isEmpty():
            p = self.tail
            q = p.next

            if p == q:
                self.tail = None
            else:
                while q.next != p:
                    q = q.next
                q.next = p.next
                self.tail = q

            self.size -= 1
            return p.data  # 삭제된 데이터

        else:
            print("Underflow")    

    def printList(self):
        p = self.tail  # 빨간 화살표

        if not self.isEmpty():
            while True:
                print("[%s] -> " % (p.next.data), end='')
                p = p.next

                if p == self.tail:
                    break
        
        print("\b\b\b   ")


if __name__=="__main__":
    L = ListType()

    L.insertLast("A"); L.printList()
    L.insertFirst("D"); L.printList()
    L.insertLast("B"); L.printList()
    L.insertLast("C"); L.printList()

    print("[%s] is deleted : " % L.deleteFirst(), end=''); L.printList()
    print("[%s] is deleted : " % L.deleteLast(), end=''); L.printList()
