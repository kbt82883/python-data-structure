from ArrayStack import ArrayStack

map = [
    ['1', '1', '1', '1', '1', '1'],
    ['e', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '1', '1', '0', '0', 'x'],
    ['1', '1', '1', '0', '1', '1'],
    ['1', '1', '1', '1', '1', '1']
]

SIZE = 6

def isValidPos(r, c):  # 행,열 번호
    if 0 <= r < SIZE and 0 <= c < SIZE:
        if map[r][c] == '0' or map[r][c] == 'x':
            return True
        
    return False

def DFS():
    print('DFS : ')
    S = ArrayStack()
    S.push((1,0))

    while not S.isEmpty():
        pos = S.pop()
        (r, c) = pos
        print(pos, end=' -> ')

        if (map[r][c] == 'x'):  # 탈출 성공
            return True
        else:  # 0이면
            map[r][c] = '.'  # 0말고 .찍어서 갔다는거 표시
            if isValidPos(r - 1, c): S.push((r - 1, c))  # 위에 갈 수 있나?
            if isValidPos(r + 1, c): S.push((r + 1, c))  # 아래
            if isValidPos(r, c - 1): S.push((r, c - 1))  # 좌
            if isValidPos(r, c + 1): S.push((r, c + 1))  # 우
            
        print(S.array[S.top::-1])

    return False


if __name__=="__main__":
    result = DFS()

    if result:
        print('Success')
    else:
        print('Fail')