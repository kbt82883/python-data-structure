class Poly:
    def __init__(self, capacity = 10):
        self.capacity = capacity  # 용량
        self.degree = 0  # 차수
        self.coef = [None] * capacity  # coeficient 계수

    def readPoly(self):
        self.degree = int(input('다항식의 차수 입력 :'))
        for i in range(self.degree, -1, -1):
            c = int(input('  %d차 항의 계수 : ' %i))
            self.coef[i] = c

    def printPoly(self):
        for i in range(self.degree, 0, -1):
            print('%dx^%d + ' %(self.coef[i], i), end='')
        print(self.coef[0])

    def add(self, other):
        result = Poly()  # 결과 다항식
        if self.degree >= other.degree:  # self의 차수가 크거나 같으면
            result.degree = self.degree  # 결과식의 차수는 self의 차수
            for i in range(self.degree, -1, -1):
                result.coef[i] = self.coef[i]
            for i in range(other.degree, -1, -1):
                result.coef[i] += other.coef[i]
        else:  # self의 차수가 작으면
            result.degree = other.degree  # 결과식의 차수는 other의 차수
            for i in range(other.degree, -1, -1):
                result.coef[i] = other.coef[i]
            for i in range(self.degree, -1, -1):
                result.coef[i] += self.coef[i]

        print("덧셈 결과 : ", end='')
        result.printPoly()

        return result
    
    def eval(self, x):
        result = 0

        for i in range(self.degree, 0, -1):
            result += self.coef[i] * x ** i
        result += self.coef[0]
        print("x=%d, 계산값 :" % x, result)

        return result

if __name__ == '__main__':
    a = Poly()
    a.readPoly()
    a.printPoly()

    a.eval(3)  # x의 값이 3
   
    b = Poly()
    b.readPoly()
    b.printPoly()
    a.add(b)  # a 더하기 b