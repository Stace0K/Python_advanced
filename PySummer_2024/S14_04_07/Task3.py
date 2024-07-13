# Задание №3
# Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import unittest

import string


class TestCaseName(unittest.TestCase):
    def test_no_change(self):
        self.assertEqual('one two', remove_symbols('one two'))

    def test_lower(self):
        self.assertEqual('one two', remove_symbols('One Two'))

    def test_punctuation(self):
        self.assertEqual('one two', remove_symbols('one, two'))

    def test_languages(self):
        self.assertEqual('one two ', remove_symbols('one two три'))

    def test_all(self):
        self.assertEqual('one two  four', remove_symbols('one two три, FOUR%'))


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
    unittest.main(verbosity=2)