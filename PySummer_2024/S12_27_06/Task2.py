# Задание №2 Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.

from collections import deque
import json
import time


class Factorial:

    def __init__(self, k: int = 1) -> None:
        self.memory = deque(maxlen=k)

    def __call__(self, num: int = 1):
        if num < 0:
            raise ValueError('Задано отрицательное значение!')
        else:
            result = 1
            for i in range(2, num + 1):
                result *= i
            self.memory.append({num: result})
        return result
        # return self.memory[-1]

    def get_memory(self):
        return self.memory

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.memory)
        print(list(self.memory))
        with open(f'{time.time()}.json', 'w', encoding='utf-8') as f:
            json.dump(list(self.memory), f)


if __name__ == '__main__':
    f1 = Factorial(3)
    f1(3)
    f1(5)
    f1(2)
    f1(6)
    f1(4)
    f1(9)
    print(f1.get_memory())
    f2 = Factorial(10)
    f2(7)
    f2(8)
    f2(1)
    f2(2)
    f2(4)
    f2(9)
    print(f1.get_memory())
    print(f2.get_memory())

    with f1 as fact:
        print(fact(10))