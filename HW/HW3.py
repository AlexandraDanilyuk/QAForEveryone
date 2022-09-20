# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3 - готово
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(*my_list[2])

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел, - готово
#    - распечатайте все строки, где есть буква 'a'
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# result = list(filter(lambda x: isinstance(x, int), list_1))
# print(sum(result))
# result2 = list(filter(lambda x: isinstance('a', str), list_1))
# print(result2)
# print(sum(number))

# Альтернативные решения
# sum1 = 0
# for i in list_1:
#     if type(i) == int:
#         sum1 += i
# print(sum1)

# print(sum([x for x in list_1 if type(x) == int]))
# print(*[y for y in list_1 if type(y) == str and 'a' in y])

# 3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж - готово

# my_list = ['cat', 'dog', 'horse', 'cow']
# tpl = tuple(my_list)
# print(type(tpl))

# 3.4. Напишите программу, которая определяет, какая семья больше. - готово
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
# family_1 = input()
# family_2 = input()
# my_list1 = family_1.split(',')
# my_list2 = family_2.split(',')
# if (len(my_list1)) > (len(my_list2)):
#     print(my_list1)
# elif (len(my_list2)) > (len(my_list1)):
#     print(my_list2)
# else:
#     print ('Equal')
#
# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию - готово
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение

# film = {
#     'title': 'Fight Club',
#     'director': 'David Fincher',
#     'year': 1999,
#     'budger': '63000000',
#     'main_actor': 'Edvard Norton',
#     'slogan': 'Интриги. Хаос. Мыло'
# }
# print(*film.keys()) # посмотреть ключи
# print(*film.values()) # посмотреть значение
# print(*film.items())
#
# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21} - готово
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# print(sum(my_dictionary.values()))
#
# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1] - готово
# print(set([1, 2, 3, 4, 5, 3, 2, 1]))

# list1 = [1, 2, 3, 4, 5, 3, 2, 1]
# ints_list1 = list(set(list1))
# print(*ints_list1)

# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785} - готово
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set2.intersection(set1)) # возврат повторяющихся значенией
# print(set2.difference(set1)) # возврат разных значенией
# print(set1.issubset(set2))
# print(set2.issubset(set1))# проверка подмножества

