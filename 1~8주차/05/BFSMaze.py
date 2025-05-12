from CircularQueue import CircularQueue

map = [
['1', '1', '1', '1', '1', '1'],
['e', '0', '1', '0', '0', '1'],
['1', '0', '0', '0', '1', '1'],
['1', '0', '1', '0', '1', '1'],
['1', '0', '1', '0', '0', 'x'],
['1', '1', '1', '1', '1', '1']
]

SIZE = 6

def isValidPos(r, c):  # 행,열 번호
    if 0 <= r < SIZE and 0 <= c < SIZE:
        if map[r][c] == '0' or map[r][c] == 'x':
            return True
        
    return False

def BFS():
    print('BFS : ')
    Q = CircularQueue()
    Q.enqueue((1,0))

    while not Q.isEmpty():
        pos = Q.dequeue()
        (r, c) = pos
        print(pos, end=' -> ')

        if (map[r][c] == 'x'):  # 탈출 성공
            return True
        else:  # 0이면
            map[r][c] = '.'  # 0말고 .찍어서 갔다는거 표시
            if isValidPos(r - 1, c): Q.enqueue((r - 1, c))  # 위에 갈 수 있나?
            if isValidPos(r + 1, c): Q.enqueue((r + 1, c))  # 아래
            if isValidPos(r, c - 1): Q.enqueue((r, c - 1))  # 좌
            if isValidPos(r, c + 1): Q.enqueue((r, c + 1))  # 우
            
        print(Q.array[Q.front + 1:Q.rear + 1])

    return False


if __name__=="__main__":
    result = BFS()

    if result:
        print('Success')
    else:
        print('Fail')