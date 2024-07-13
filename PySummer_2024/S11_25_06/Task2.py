# Задание №2 Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

class Archive:
    _instance = None

    def __new__(cls, num, string):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_nums = []
            cls._instance.archive_strings = []
        else:
            cls._instance.archive_nums.append(cls._instance.num)
            cls._instance.archive_strings.append(cls._instance.string)
        return cls._instance

    def __init__(self, num, string):
        self.num = num
        self.string = string


a = Archive(5, 'gfh')

b = Archive(2, 'od')
c = Archive(8, 'ghjhk')
d = Archive(4, 'tytui')
print(b.archive_nums)
print(a.archive_nums)
print(c.archive_nums)
print(Archive._instance)
print(d.num)