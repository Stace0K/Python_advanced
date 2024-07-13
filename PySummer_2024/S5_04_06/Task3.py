# Задание №3
# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

text = 'В лесу родилась елочка'
my_dict = {char: ord(char) for char in text if char != ' '}
print(my_dict)
count = 5
my_iter = iter(my_dict.items())
for _ in range(count):
    print(next(my_iter))