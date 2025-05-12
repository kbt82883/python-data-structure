from ArrayStack import ArrayStack

def evalPostfix(expr):  # 수식을 받아서 후위연산, 후위표기식
    S = ArrayStack()

    for term in expr:  # ['8', '2', '/', ... ]
        if term in '+-*/':  # 연산자이거나
            val2 = S.pop()  # 먼저 pop한게 연산자의 오른쪽
            val1 = S.pop()

            if term == '+': S.push(val1 + val2)
            elif term == '-': S.push(val1 - val2)
            elif term == '*': S.push(val1 * val2)
            elif term == '/': S.push(val1 / val2)

        else:  # 숫자이거나
            S.push(float(term))  # 나누기땜에 실수 계산이 있으니까

    return S.pop()  # 스택에 남은 최종 결과값

if __name__=="__main__":
    str = '8 2 / 3 - 3 2 * +'
    expr = str.split()

    print(str, ' --> ', evalPostfix(expr))