class ArrayStack:
    
    def __init__(self, capacity = 30):
        self.capacity = capacity
        self.top = -1
        self.array = [None] * capacity

    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.capacity -1
    
    def push(self,e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e
        else:
            print('Overflow.')

    def pop(self):
        if not self.isEmpty():
            e = self.array[self.top]
            self.top -= 1
            return e
        else:
            print('Underflow.')

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            print('Underflow.')

    def display(self):  # 동작을 확인을 위한, 원래는 스택 중간을 볼 수 있으면 안됨
        print()
        for i in range(self.top, -1, -1):
            print(' | %d |' % self.array[i])
            print(' -----')
        print()

if __name__=="__main__":
    S = ArrayStack()
    data = [5, 3, 8, 1, 2, 7]

    for e in data:
        S.push(e)
    S.display()

    print('[%d] is popped.' % S.pop())
    S.display()

    print('[%d] is peeked.' % S.peek())
    S.display()