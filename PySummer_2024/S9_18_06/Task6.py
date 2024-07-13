# Задание №6
# Доработайте прошлую задачу добавив декоратор wraps в
# каждый из декораторов.
import json
import os
from typing import Callable
from functools import wraps
from random import randint


def counter(num: int):
    def deco(func: Callable):
        my_list = []

        @wraps(func)
        def wrapper(*args, **kwargs):

            for _ in range(num):
                my_list.append(func(*args, **kwargs))
            return my_list

        return wrapper

    return deco


def number_control(fun: Callable) -> Callable:
    min_attempts = 1
    max_attempts = 10
    min_guessing = 1
    max_guessing = 100

    # def wrapper(*args, **kwargs): вариант 1
    @wraps(fun)
    def wrapper(gues: int, att: int, *args, **kwargs):
        guessing = gues if min_guessing <= gues <= max_guessing else randint(min_guessing, max_guessing)
        attempts = att if min_attempts <= att <= max_attempts else randint(min_attempts, max_attempts)
        return fun(guessing, attempts)

    return wrapper


def deco_json(func):
    filename = f'{func.__name__}.json'
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='utf-8') as f_r:
            data = json.load(f_r)
            print(data)
    else:
        data = []

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        json_dict = {'result': result, 'args': args, **kwargs, }
        data.append(json_dict)
        with open(filename, 'w', encoding='utf-8') as f_w:
            json.dump(data, f_w, indent=4, ensure_ascii=False)

        return result

    return wrapper


@counter(3)
@number_control
@deco_json
def guessing_game(guessing: int, attempts: int, x=10):
    for i in range(attempts):
        print(f'Ваша попытка № {i + 1}')
        var = int(input('Угадай число: '))
        if var == guessing:
            print('Вы угадали, браво!!')
            return
    print('Количество попыток исчерпано!')
    return


if __name__ == '__main__':
    #print(guessing_game.__name__)
    guessing_game(200,300)

