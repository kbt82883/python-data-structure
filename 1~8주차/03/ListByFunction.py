capacity = 100
size = 0
array = [None] * capacity

def isEmpty():
    return size == 0

def isFull():
    return size == capacity

def insert(pos,e):  # 포지션, 엘리먼트
    global size  # 함수안에서 size변수 쓸거야
    if not isFull() and 0 <= pos <=size:  # 사이즈보다 몇칸 띄어서 삽입하면 안됨
        for i in range(size, pos, -1):
            array[i] = array[i-1]  # 오른쪽으로 하나씩 밀기
        array[pos] = e
        size += 1  # 사이즈 늘음
    else:
        print("Overflow or Invalid Position.")

def delete(pos):
    global size  # 함수안에서 size변수 쓸거야
    if not isEmpty() and 0 <= pos < size:  # 사이즈보다 몇칸 띄어서 삽입하면 안됨
        e = array[pos]
        for i in range(pos, size-1):  # 왼쪽으로 하나씩 덮어쓰기
            array[i] = array[i+1]
        size -= 1  # 사이즈 줄음
        return e
    else:
        print("Underflow or Invalid Position.")

def getEntry(pos):
    if 0 <= pos < size:  #배열 사이즈 안의 pos이면
        return array[pos]
    else:
        return None

if __name__ == "__main__":
    insert(0,"A")
    insert(1,"B")
    insert(1,"C")
    print(array[0:size])

    insert(4,"D")
    insert(3,"E")
    print(array[0:size])

    print("[%c] is deleted." % delete(3))
    print(array[0:size])