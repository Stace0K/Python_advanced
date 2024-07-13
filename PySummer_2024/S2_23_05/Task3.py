# Задание №3
# Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов, где это возможно

BIN = 2
OCT = 8

num: int = int(input('Enter a number:\n'))
print(bin(num), oct(num), hex(num))

for div in (BIN, OCT):
    new_num = num
    result: str = ''
    while new_num:
        result = str(new_num % div) + result
        new_num //= div
    print(result)