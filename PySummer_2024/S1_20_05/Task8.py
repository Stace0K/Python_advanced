# Задание №8
# Нарисовать в консоли ёлку, спросив
# у пользователя количество рядов.

# range(start=0, stop, step=1)#
#
# range(5) -> range(start=0, stop=5, step=1) -> 0,1,2,3,4
# range(2, 10) -> range(start=2, stop=10, step=1) -> 2,3,4,5,6,7,8,9
# range(3, 15, 2) -> range(start=3, stop=15, step=2) -> 3,5,7,9,11,13

SPACE = " "
STAR = "*"

rows = int(input('Number of rows: '))
spaces = rows - 1
stars = 1

for _ in range(1, rows):
    print(f'{SPACE * spaces}{STAR * stars}')
    stars += 2
    spaces -= 1

SPACE = " "
STAR = "*"