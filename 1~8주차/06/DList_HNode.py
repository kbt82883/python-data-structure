# 이중연결리스트의 헤드 노드 버전

class Node:
    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev  # 이전 노드도 받음
        self.next = next

class DListType:
    def __init__(self):  # 차이점1 : 초기화가 다름
        self.head = Node(0)  # 앞뒤 노드 만들어두고, 의미없는 데이터 넣어둠
        self.tail = Node(0)
        self.head.next = self.tail  # 앞뒤 노드가 서로를 가리키는 상태로 초기화
        self.tail.prev = self.head
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    # def isFull 은 없음, 용량이 없어서

    def insert(self, pos, data):
        if pos <= 0 or pos > self.size + 1:
            print("Invalid Pos")
            return
        
        # 화살표를 선생님한테 바로 가리킬 수 없어서
        # 다른 거에서는 insertFirst가 따로 있음
        # 차이점2 : 초기화된 학생이 있어서, insert가 바로 됨
        p = self.head

        for _ in range(1, pos):
            p = p.next

        node = Node(data)
        # 노드 만들고 4가지 지정하기
        node.prev = p
        node.next = p.next
        p.next.prev = node
        p.next = node

        self.size += 1

    def delete(self, pos):
        if pos <= 0 or pos > self.size:
            print("Invalid Pos")
            return
        
        p = self.head

        for _ in range(pos):  # insert보다 한번 더 움직임
            p = p.next

        data = p.data

        p.prev.next = p.next
        p.next.prev = p.prev

        self.size -= 1

        return data


    def printList(self):
        p = self.head.next

        while p != self.tail:
            print("[%s] <-> " % p.data, end="")
            p = p.next
        print("\b\b\b\b    ")

# 이중연결리스트에서 insertFirst, insertLast는 pos만 특정 값일때로 하면 됨
# 따로 해보시고요~ (시험 나올라나)
if __name__=="__main__":
    DL = DListType()

    DL.insert(1,"A"); DL.printList()
    DL.insert(1,"B"); DL.printList()
    DL.insert(2,"C"); DL.printList()
    DL.insert(4,"D"); DL.printList()

    print("[%s] is deleted." % DL.delete(3)); DL.printList()