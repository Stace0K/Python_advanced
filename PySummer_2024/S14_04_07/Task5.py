# Задание 5
# На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину,
# а также вычисляющую периметр, площадь и позволяющий складывать и
# вычитать прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.
import unittest


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.r1 = Rectangle(1, 1)
        self.r2 = Rectangle(10, 20)
        self.r3 = Rectangle(20, 10)
        self.r4 = Rectangle(3, 2)

    def test_area(self):
        self.assertEqual(self.r3.square(), 200)

    def test_perimeter(self):
        self.assertEqual(self.r2.perimeter(), 60)

    def test_add(self):
        self.assertEqual(self.r2 + self.r3, Rectangle(30, 30))

    def test_sub(self):
        self.assertEqual(self.r4 - self.r1, Rectangle(2, 1))

    def test_perimeter_equal(self):
        self.assertEqual(self.r2.perimeter(), self.r3.perimeter())

    def test_area_noequal(self):
        self.assertNotEqual(self.r1.square(), self.r3.square())

    def test_create(self):
        self.assertEqual(Rectangle(3, 2), self.r4)


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
    unittest.main(verbosity=2)