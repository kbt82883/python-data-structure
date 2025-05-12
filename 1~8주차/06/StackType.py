class Node:  # 학생 노드
    def __init__(self, data, next = None):  # 데이터와 뒷 노드, next초기값도 필요없긴함함
        self.data = data
        self.next = next

class StackType:
    def __init__(self):
        # 헤드포인터 = 제일 첫 학생을 가르킴
        self.top = None  # 선생 노드, 아직 아무도 없음
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    # def isFull 은 없음, 용량이 없어서

    def push(self, data):  # 선생 헤드라서(p가 선생을 못 가리켜서) inserFirst는 따로 만드는듯?
        node = Node(data)  # 학생 등장, 첫번째 노드를 가리킴
        node.next = self.top
        self.top = node  # 선생님이 잡음
        self.size += 1

    def getNode(self, pos):
        p = self.head  # 화살표가 첫번째 노드를 가리킴
            
        for _ in range(1, pos-1):  # pos가 3이면 화살표가 한번 움직이고 두번째 노드를 가리킴
            p = p.next  # pos의 전 노드 위치를 찾기

        return p

    def pop(self):
        if not self.isEmpty():
            p = self.top  # 빨간 화살표 첫번째 노드
            self.top = p.next
            self.size -= 1
            return p.data
        else:
            print("Underflow")

    def printList(self):
        p = self.top  # 첫번째 노드, 빨간 화살표

        while p != None:
            print(' | [%s] | ' % (p.data))
            print("  ----  ")
            p = p.next  # 다음 학생으로 화살표 옮김

        print('\b\b\b   ') 

if __name__=="__main__":
    S = StackType()  # L반

    S.push('A')
    S.push('B')
    S.push('C'); S.printList()

