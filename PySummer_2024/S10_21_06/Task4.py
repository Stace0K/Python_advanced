"""
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания.
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления
суммы цифр _id на семь
"""
import random


class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.__age = age

    def birthday(self):
        self.__age += 1

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_age(self):
        return self.__age


class Worker(User):

    def __init__(self, first_name, last_name, age):
        User.__init__(self, first_name, last_name, age)
        self._id = random.randint(10**5, 10**6)
        self._level = sum(int(i) for i in str(self._id)) % 7

    def get_id(self):
        return self._id

    def get_level(self):
        return self._level


if __name__ == '__main__':
    work_1 = Worker('Ivan', 'Ivanov',44)
    print(work_1.get_id(), work_1.get_level())
    print(work_1.full_name())