# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
# def square(length):
#     a = 4 * length
#     b = length * length
#     c = (2 * (length ** 2)) ** 0.5 #
#     return a, b, c
# print(square(10))
#
# 4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
# def person(name, last_name, age, position):
#     return f'name: {name} \n last_name: {last_name}  \n age: {age}  \n position: {position}'
# print(person('John', 'Smith', 35, 'web developer'))

# Чужое решение

# def name_arg (**kwargs):
#     for key, value in kwargs.items():
#         print('{}: {}'.format(key, value))
#
# name_arg(name = 'John', last_nane = 'Smith', age = 35, position = 'web developer')
#
# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа

# my_list = [20, -3, 15, 2, -1, -21]
# result1 = list(filter(lambda x: x >= 0, my_list))
# print(result1)

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# from functools import reduce
# result2 = reduce(lambda x, y: x*y, result1)
# print(result2)

# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.

# from my_calc import *
# res1 = sum_it(5, 8)
# print(res1)
#
# res2 = prod(5, 8)
# print(res2)
#
# res3 = div(5, 8)
# print(res3)
#
# res4 = minus(5, 8)
# print(res4)