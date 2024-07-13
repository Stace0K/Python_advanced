# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.

from math import pi


class Circle:
    def __init__(self, r=12):
        self.r = r

    def square(self):
        return pi * self.r ** 2

    def length(self):
        return 2 * pi * self.r


if __name__ == '__main__':
    circle_1 = Circle()
    print(circle_1.square(), circle_1.length())