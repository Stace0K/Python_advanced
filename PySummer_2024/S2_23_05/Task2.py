# Задание №2
# Создайте в переменной data список значений разных типов, перечислив их через запятую внутри квадратных скобок.
# Для каждого элемента в цикле выведите:
# порядковый номер начиная с единицы,
# значение,
# адрес в памяти,
# размер в памяти,
# хэш объекта,
# результат проверки на целое число, только если он положительный,
# результат проверки на строку, только если он положительный.
# Добавьте в список повторяющиеся элементы и сравните на результаты.

import sys
import typing

a = 256
# data = [1, 2.3, 'Hellow world!', {'key1': 83}, (1, [2], 3), True, 2.3]
data = [a, 256, 73.0, 'Hello world!', True, 42, 'Hello world!', 256, 2 ** 8, 1, 'Привет, мир!', 73.0]
for i, item in enumerate(data, start=1):
    check_int = 'Это число' if isinstance(item, int) else ''
    check_str = 'Это строка' if isinstance(item, str) else ''
    # check_hash = 'Не хэшируем' if isinstance(item, (dict, list, set)) else
    # hash(item)
    # check_hash = 'Не хэшируем' if not isinstance(item, typing.Hashable) \
    #     else hash(item)
    try:
        check_hash = hash(item)
    except TypeError:
        check_hash = 'Нехэшируемый'

    print(
        f"{i=}, {item=}, {id(item)=}, {sys.getsizeof(item)=}, "
        f"{item.__sizeof__()=}, {check_hash=}, {check_int=}{check_str=}"
    )

print(id(a))