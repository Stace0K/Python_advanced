# Задание №6
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

value = input("Enter some words:\n").split()
max_len = max(len(item) for item in value)

max_len = 0
for item in value:
    if len(item) > max_len:
        max_len = len(item)

value.sort()
for i, item in enumerate(value, 1):
    print(f'{i} {item:>{max_len}}')