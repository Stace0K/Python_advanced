# Задание №2
# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

def get_dict(cur_dict, key, default=0):
    try:
        if not isinstance(cur_dict, dict):
            raise TypeError
    except TypeError:
        #print('Аргумент не является словарем!')
        return 'Аргумент не является словарем!'
    try:
        return cur_dict[key]
    except KeyError as e:
        return default


if __name__ == '__main__':
    my_dict = {'1': 1, '2': 2, '3': 3}
    my_dict2 = 23
    # print(get_dict(my_dict, '1'))
    # print(get_dict(my_dict, '4'))
    # print(get_dict(my_dict, '4', None))
    print(get_dict(my_dict2, '4'))