# Задание №3
# Добавьте к задачам 1 и 2 строки документации для классов.

class Archive:
    """Та еще задачка"""
    num_arch, string_arch = [], []

    def __init__(self, num, string):
        """Та еще функция. В той еще задаче"""

        self.num = num
        self.string = string
        self.num_arch.append(num)
        self.string_arch.append(string)


a = Archive(5, 'gfh')
print(a.num_arch)
b = Archive(2, 'od')

print(b.num_arch)
print(a.num_arch)
print(Archive.num_arch, Archive.string_arch)
print(Archive.__doc__)
print(Archive.__init__.__doc__)
print(help(Archive))