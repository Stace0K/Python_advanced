# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

import datetime


class MyStr(str):
    def __init__(self, *args, **kwargs):
        print('Сработал метод init', args)

    def __new__(cls, text, author):

        instance = super().__new__(cls, text)
        instance.author = author
        instance.time = datetime.datetime.now()
        print('Сработал метод new', instance.author, instance.time, instance)
        return instance





print('Начало программы')
a = MyStr('hello', 'Tartt')
b = MyStr('bay', 'Pivkin')
c = MyStr('goodBay', 'Klein')
d = MyStr('bu bu bu', 'people')
e = a
print(a, b, c, d, e)
print(a.author, b.time, c, d, e)
print(issubclass(MyStr, str))
print(issubclass(str, MyStr))
print(isinstance(str(), MyStr))
print(isinstance(a, str))

