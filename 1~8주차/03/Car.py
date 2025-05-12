class Car:
    def __init__(self, color, speed = 0):
        self.color = color
        self.speed = speed

    def speedUP(self):
        self.speed += 10

    def speedDown(self):
        self.speed -= 10

    def __str__(self):
        return "Color : %s - Speed : %d" %(self.color, self.speed)

if __name__ == '__main__':
    car1 = Car('Black')
    car2 = Car('Red', 50)

    print(car1)
    print(car2)

    car2.speedDown()
    print(car2)