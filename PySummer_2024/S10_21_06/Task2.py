"""
Создайте класс прямоугольник.
Класс должен принимать длину и ширину при создании
экземпляра.
У класса должно быть два метода, возвращающие периметр
и площадь.
Если при создании экземпляра передаётся только одна
сторона, считаем что у нас квадрат.
"""


class Rectangle:

    def __init__(self, a, b=None):
        self.a = a
        self.b = b if b else a

    def square(self):
        return self.a * self.b

    def perimetr(self):
        return 2 * self.a + 2 * self.b


if __name__ == '__main__':
    rect_1 = Rectangle(4)
    rect_2 = Rectangle(2, 7)
    print(rect_1.square(), rect_1.perimetr())
    print(rect_2.square(), rect_2.perimetr())