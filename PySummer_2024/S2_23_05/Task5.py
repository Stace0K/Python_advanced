# Задание №5
# Напишите программу, которая решает квадратные уравнения даже если
# дискриминант отрицательный.
# Используйте комплексные числа
# для извлечения квадратного корня.

a = 2
b = 3
c = 3

d = (b**2 - 4 * a * c) # discriminant
x1 = (-b + d ** .5) / (2 * a)
x2 = (-b - d ** .5) / (2 * a)

print(x1, x2)