"""Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
Например, отлавливаем ошибку деления на ноль.
"""

import logging
import datetime


FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" ' \
    'в строке {lineno:03d} функция "{funcName}()" ' \
    'в {created} секунд записала сообщение: {msg}'
logging.basicConfig(format=FORMAT, style='{', level=logging.ERROR, filemode='w', filename='error_1.log', encoding='utf-8')
logger = logging.getLogger('task_01')


def div_func(a, b):
    res = float('inf')
    try:
        res = a / b
    except ZeroDivisionError:
        logger.error('На ноль делить нельзя')
    return res


if __name__ == '__main__':
    print(div_func(3, 0))