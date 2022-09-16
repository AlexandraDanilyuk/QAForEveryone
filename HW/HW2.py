# Задание 1
# health = int(input('You health:'))
# if health <= 0:
#     print('False')
# else:
#     print('True')

# def task2_1(health): - чужое решение
#        print(health > 0)  - не поняла как через консоль вызвать ответ

# i = int(input('Number:'))
# if i % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')

# i = int(input('Year:'))
# if i % 400 == 0:
#     print('Високосный')
# elif i % 100 == 0:
#     print('Не високосный')
# elif i % 4 == 0:
#     print('Високосный')
# else:
#     print('Не високосный')

# i = int(input('Year:'))
# a = 'Високосный'
# b = 'Не високосный'
# if i % 400 == 0:
#     print(a)
# elif i % 100 == 0:
#     print(b)
# elif i % 4 == 0:
#     print(a)
# else:
#     print(b)

# i = int(input('Year:'))  - чужое решение покороче с логическим И
# if i % 4 == 0 and i % 100:
#     print('Високосный')
# elif i % 400 == 0:
#     print('Високосный')
# else:
#     print('Не високосный')

# i = int(input('Year:'))  # чужое решение в одно условие
# if (i % 4 == 0 and i % 100 !=0 or i % 400):
#     print('Високосный')
# else:
#     print('Не високосный')

text = input('Your text:')
for i in range(int(input('Number:'))):
       print(text) #в столбик
       print(text, end=' ') # в строку

# text = input('Your text:') - чужое решение через вайл
# time = (int(input('Times:')))
# i = 0
# while i < time:
#     print(text)
#     i +=1