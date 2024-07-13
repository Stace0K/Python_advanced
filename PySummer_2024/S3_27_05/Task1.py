# Задание №1 Вручную создайте список с целыми числами, которые повторяются.
# Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
# *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.

data = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]

print(list(set(data)))

my_list = []
for item in data:
    if item not in my_list:
        my_list.append(item)

print(my_list)
my_list = []
print([my_list.append(item) for item in data if item not in my_list])
print(my_list)
my_list = [item ** 2 for item in data]
print(my_list)
my_list = [item if item not in my_list else 0 for item in data]

my_set = {item ** 2 for item in data}
my_dict = {item: item ** 2 for item in data}
my_gen = (item ** 2 for item in data)