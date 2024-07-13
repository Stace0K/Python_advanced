# Задание №7
# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например, 5 - 25
# Для двузначного числа произведение цифр, например, 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

LOWER_LIMIT = 1
UPPER_LIMIT = 999
ONE = 1
TEN = 10
HUNDRED = 100

number = LOWER_LIMIT - ONE

while number < LOWER_LIMIT or number > UPPER_LIMIT:
    number = int(input(f'Number ({LOWER_LIMIT} - {UPPER_LIMIT}): '))

if number < TEN:
    result = f'Square = {number * number}'
elif number < HUNDRED:
    product = (number // TEN) * (number % TEN)
    result = f'The result of multiplication a two-digit number = {product}'
else:
    mirror = (number % TEN * HUNDRED) + (number // TEN % TEN * TEN) + (number // HUNDRED)
    result = f'The result of mirroring a three-digit number = {mirror}'

print(f'{result}')