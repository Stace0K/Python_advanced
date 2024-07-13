# Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import string


def remove_symbols(text: str) -> str:
    """
    Удаляет из текста все символы, кроме букв латинского алфавита и пробелов.
    >>> remove_symbols('one two')
    'one two'
    >>> remove_symbols('One Two')
    'one two'
    >>> remove_symbols('one, two')
    'one two'
    >>> remove_symbols('one two три')
    'one two '
    >>> remove_symbols('one two три, FOUR%')
    'one two  four'
    """

    return ''.join(letter for letter in text if letter in string.ascii_letters + " ").lower()


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)