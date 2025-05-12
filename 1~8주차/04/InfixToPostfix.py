from ArrayStack import ArrayStack

def order(op):  # 연산자 우선순위
    if (op == '(' or op == ')'): return 0
    elif (op == '+' or op == '-'): return 1
    else: return 2  # */이면 우선순위 높음

def infixToPostfix(expr):
    S = ArrayStack()
    postfix = []

    for term in expr:
        if term in '(':  # 일단 푸시
            S.push(term)
        elif term in ')':  # ( 나올때 까지 전부 팝
            while not S.isEmpty():  # 스택이 안 비어있으면
                op = S.pop()
                if op == '(':
                    break
                else:
                    postfix.append(op)
        elif term in '+-*/':
            while not S.isEmpty():  # 스택이 안 비어있으면
                op = S.peek()
                if (order(term) <= order(op)):  # 지금 들어가려는 연산이 스택 맨위의 연산자보다 우선순위가 낮으면
                    postfix.append(S.pop())
                else:
                    break
            S.push(term)
        else:  # term이 부호가 아니라 숫자
            postfix.append(term)

    while not S.isEmpty():  # 끝났는데도 남아있으면
        postfix.append(S.pop())

    return postfix

if __name__=="__main__":
    infix = input("Input Infix Expr... ")
    expr = infix.split()
    postfix = infixToPostfix(expr)

    print(postfix)