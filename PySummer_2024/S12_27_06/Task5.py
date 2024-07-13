# Задание №5 Доработаем прямоугольник и добавим экономию памяти для хранения свойств
# экземпляра без словаря __dict__.

class Rectangle:
    __slots__ = ("_length", "_width")

    def __init__(self, length, width=None):
        self._length = length
        self._width = width if width else length

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value > 0:
            self._length = value
        else:
            raise ValueError("Value cannot be less than zero\n")

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError("Value cannot be less than zero\n")

    def square(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __add__(self, other):
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        length = perimeter / 2 - width
        return Rectangle(length, width)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        length = perimeter / 2 - width
        return Rectangle(length, width)

    def __eq__(self, other):
        return self.square() == other.square()

    def __gt__(self, other):
        return self.square() > other.square()

    def __ge__(self, other):
        return self.square() >= other.square()


if __name__ == '__main__':
    a = Rectangle(25, 5)
    b = Rectangle(10, 9)
    a.width = 8
    print(a.width)
    print(a.__dict__)