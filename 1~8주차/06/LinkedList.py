# 단순연결리스트도 헤드노드버전으로 해보세요 (시험나오나)

class Node:  # 학생 노드
    def __init__(self, data, next = None):  # 데이터와 뒷 노드, next초기값도 필요없긴함함
        self.data = data
        self.next = next

class ListType:
    def __init__(self):
        # 헤드포인터 = 제일 첫 학생을 가르킴
        self.head = None  # 선생 노드, 아직 아무도 없음
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    # def isFull 은 없음, 용량이 없어서

    def insertFirst(self, data):  # 선생 헤드라서(p가 선생을 못 가리켜서) inserFirst는 따로 만드는듯?
        node = Node(data, self.head)  # 학생 등장, 첫번째 노드를 가리킴
        self.head = node  # 선생님이 잡음
        self.size += 1

    def getNode(self, pos):
        p = self.head  # 화살표가 첫번째 노드를 가리킴
            
        for _ in range(1, pos-1):  # pos가 3이면 화살표가 한번 움직이고 두번째 노드를 가리킴
            p = p.next  # pos의 전 노드 위치를 찾기

        return p

    def insert(self, pos, data):
        if pos == 1:
            self.insertFirst(data)
        else:
            if pos <= self.size + 1:
                p = self.getNode(pos)

                node = Node(data, p.next)  # 난 누굴 가리키지
                p.next = node  # 누가 날 가리키지
                self.size += 1
            else:
                print('Invalid Pos')

    def deleteFirst(self):
        if not self.isEmpty():
            p = self.head  # 빨간 화살표 첫번째 노드
            self.head = p.next
            self.size -= 1
            return p.data
        else:
            print("Underflow")

    def delete(self, pos):
        if pos <= 0 or pos > self.size:
            print("Invalid Pos")
            return
        
        if not self.isEmpty():
            if pos == 1:
                return self.deleteFirst()
            else:
                q = self.getNode(pos)  # 3번 없앨거면 2번 노드를 가리킴
                p = q.next  # 3번 노드를 가리키네

                q.next = p.next
                self.size -= 1

                return p.data

    def printList(self):
        p = self.head  # 첫번째 노드, 빨간 화살표

        while p != None:
            print('[%s] -> ' % (p.data), end='')
            p = p.next  # 다음 학생으로 화살표 옮김

        print('\b\b\b   ')        

if __name__=="__main__":
    L = ListType()  # L반

    L.insertFirst('A'); L.printList()
    L.insertFirst('B'); L.printList()

    L.insert(1, "C"); L.printList()
    L.insert(4, "D"); L.printList()
    L.insert(3, "E"); L.printList()

    print("[%s] is deleted : " % L.deleteFirst(), end=''); L.printList()
    print("[%s] is deleted : " % L.delete(3), end=''); L.printList()
