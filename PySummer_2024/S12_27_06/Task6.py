# Задание №6
# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

class CheckValues:
    def __init__(self, min_value, max_value):
        print("Step CheckValues init")
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        print("Step CheckValues set_name")
        self.param_name = '_' + name
        print(self.param_name)

    def __get__(self, instance, owner):
        print("Step CheckValues get")
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        print("Step CheckValues set")
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        print("Step CheckValues validate")
        if self.min_value > value or value > self.max_value:
            raise ValueError("Value is out of set range\n")


class Rectangle:
    # __slots__ = ("_length", "_width")

    _length = CheckValues(0, 100)
    _width = CheckValues(0, 50)

    def __init__(self, length, width=None):
        print("Step init")
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

    @property
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
    a = Rectangle(100, 23)
    b = Rectangle(10, 9)
    a.width = 8
    print(a.width)
    # print(a.perimeter)