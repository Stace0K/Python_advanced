# Задание №1 Создайте функцию, которая удаляет из текста все символы, кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

import string
import re


def remove_symbols(text: str) -> str:
    # return re.sub(r'[^a-zA-Z ]', '', text).lower()
    # result_string = ''
    # for letter in text:
    #     if letter in string.ascii_letters + " ":
    #         result_string += letter
    # return result_string.lower()
    return ''.join(letter for letter in text if letter in string.ascii_letters + " ").lower()


if __name__ == '__main__':
    my_text = ('The wrapper function performs additional tasks (reading the CSV). '
               '1 2 3 Миру мир! %')
    print(remove_symbols(my_text))