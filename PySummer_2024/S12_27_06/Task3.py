# Задание №3
# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

from collections import deque
import json


class Factorial:

    def __init__(self, *args) -> None:
        self.start = 1
        self.stop = 1
        self.step = 1

        match len(args):
            case 1:
                self.stop = args[0]
            case 2:
                self.start, self.stop = args
            case 3:
                self.start, self.stop, self.step = args
            case _:
                raise ValueError("Too many parameters\n")

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.stop:
            result = 1
            for mult in range(1, self.start + 1):
                result *= mult
            temp = self.start
            self.start += self.step
            return {temp: result}
        raise StopIteration


if __name__ == '__main__':
    f1 = Factorial(3, 6)
    for item in f1:
        print(item)