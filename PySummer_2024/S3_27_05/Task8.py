# Задание №8
# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# Какие вещи взяли все три друга
# Какие вещи уникальны, есть только у одного друга
# Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

hike = {
    'Ваня': ('спички', 'нож', 'парафин', 'веревка', 'рюкзак'),
    'Вася': ('карта', 'компас', 'топор', 'нож', 'рюкзак', 'уголь'),
    'Петя': ('навигатор', 'мангал', 'гитара', 'спички', 'палатка', 'нож', 'топор')
    }

all_things = set()
for value in hike.values():
    all_things.update(value)

print("All things:", all_things)

unique_items = set()
dict_unique_items = {}
for friend_master, things_master in hike.items():
    cur_set = set(things_master)
    for friend_slave, things_slave in hike.items():
        if friend_master != friend_slave:
            cur_set -= set(things_slave)
    unique_items.update(cur_set)
    dict_unique_items[friend_master] = cur_set

print("Unique items: ", unique_items)
print("Dict unique items: ", dict_unique_items)

duplicate_items = all_things - unique_items

for friend, things in hike.items():
    print(f'Friend {friend} does not have {duplicate_items - set(things)} but others have')