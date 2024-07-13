# Задание №2
# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def my_func(str_in):
    print(sorted(map(ord, set(str_in)), reverse=True))


my_text = 'символа введённой строки отсортированный по убыванию'
my_func(my_text)