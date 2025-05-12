from EvalPostfix import evalPostfix
from InfixToPostfix import infixToPostfix

infix = input("Input Infix Expr... ")
expr = infix.split()

print(infix, '=', evalPostfix(infixToPostfix(expr)))