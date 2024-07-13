# Задание №1
# ✔ Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
#  хранятся в кортеже как значения второго ключа.

numbers = '10/12/1/4/28/30/35'
number_list = numbers.split('/')
key1, key2, key3 = int(number_list[0]), int(number_list[1]), int(number_list[2])
values = tuple(map(int, number_list[3:]))
my_dict = {key2: key1, key3: values}
print(my_dict)

st_list = '12/4/5/78/9/4'.split('/')
res_dic = dict()
res_dic[st_list[1]], res_dic[st_list[2]] = st_list[0], tuple(st_list[3:])
print(res_dic)

input_string = '12/4/5/78/9/4'
numbers = input_string.split('/')
if len(numbers) < 4:
    print("Ошибка: необходимо ввести минимум четыре числа.")
else:
    numbers = list(map(int, numbers))

    result_dict = {
        numbers[1]: numbers[0],
        numbers[2]: tuple(numbers[3:])
    }
print(result_dict)

str_use = '12/4/5/78/9/4'
lst_2 = [int(s) for s in str_use if s.isdigit()]
print(lst_2)
my_dict = {lst_2[1]: lst_2[0], lst_2[2]: lst_2[3::]}
print(my_dict)

one, two, three, *other = input('Какой текст преобразовать? ').split('/')
print(map(int, other))
print(tuple(map(int, other)))
result = {
    int(two): int(one),
    int(three): tuple(map(int, other)),
}
print(f'{result = }')