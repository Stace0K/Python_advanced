# Вывести в консоль таблицу умножения (как на школьной тетради)

START_NUM = 2
END_NUM = 10
COLUMNS = 4

for start_num_1 in (START_NUM, START_NUM + COLUMNS):
    for num_2 in range(START_NUM, END_NUM + 1):
        for num_1 in range(start_num_1, start_num_1 + COLUMNS):
            print(f'{num_1}  X {num_2:>2} = {num_1 * num_2:>2}', end='\t')
        print()
    print()

