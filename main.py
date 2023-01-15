# import math
#
# while True:
#     c = str(input("выберите действие : (+) (-) (*) (/) или выход что бы выйти"))
#     a = int(input("введите первое число :"))
#     b = str(input("введите второе числo :"))
#
#     if c == "выход" or c == "exit":
#         break
#     elif c == "+":
#         print(a + b)
#     elif c == "-":
#         print(a - b)
#     elif c == "*":
#         print(a * b)
#     elif c == "/":
#         print(a / c)
#     else:
#         print("вводи коректные знаки!!!")

#
# def dollar(int):
#     action = currency * 85.68
#     action = round(action, 2)
#     return action
#
#
# #
# def euro(int):
#     action2 = currency * 92.95
#     action2 = round(action2, 2)
#     return action2
#
#
# while 1:
#     input("Это программа поможет вам перевести нашу валюту в другую (Нажмите 'Enter' чтобы продолжить) ")
# #     currency = int(input('Введите сумму своей валюты '))
# #     if type(currency) == int:
# #         print(f'Ваша сумма по курсу доллара составляет {dollar(currency)}$')
# #         print(f'Ваша сумма по курсу евро составляет {euro(currency)}€')
# #     else:
# #         print('ошибка')
#
# def arithmetic(number1, number2, action):
#     if action == '+':
#         print(number1 + number2)
#     elif action == '-':
#         print(number1 - number2)
#     elif action == '*':
#         print(number1 * number2)
#     elif action == '/':
#         if number2 > 0:
#             print(number1 // number2)
#         else:
#             print('На ноль делить нельзя!!!')
#         print('Не верная операция!!!')
#     return f'return...'
#
#
# while 1:
#     first = float(int(input("Введите первое число ")))
#     second = float(int(input("Введите второе число ")))
#     user = input('Введите действие ')
#     print(arithmetic(first, second, user))
# #
# def is_year_leap(year):
#     if year % 4:
#         print(f'{year} не високосный')
#         return False
#     else:
#         print(f'{year} високосный')
#     return True
#
#
# while 1:
#     user = int(input('Введите год '))
#     print(is_year_leap(user))
# import math
#
#
# def square(line: int):
#     p = line * 4
#     s = line ** 2
#     d = math.sqrt(2 * line)
#     return f'{p} периметр\n' \
#            f'{s} площадь\n' \
#            f'{round(d, 2)} диагональ'
#
#
# print(square(5))
# def season(month):
#     if month in (12, 1, 2):
#         return "зима"
#     elif month in (3, 4, 5):
#         return "весна"
#     elif month in (6, 7, 8):
#         return "лето"
#     elif month in (9, 10, 11):
#         return "осень"
#
#
# #
# #
# while 1:
#     user = int(input('Введите номер месяца '))
#     print(season(user))

# # print((150 / 100) * 10)
# def bank(a: int, year: int):
#     god = ((a / 100) * 10) + a
#     return f'Через {year} лет(год) Ваша сумма будет составлять: {round(year * god, 2)}'
#
#
# while 1:
#     user = int(input('Введите вашу сумму '))
#     let = int(input('Введите ваш год хранения '))
#     print(bank(user, let))
#
# def is_prime(number):
#     d = 2
#     while number % d != 0:
#         d += 1
#     return d == number
#
#
# while 1:
#     user = int(input('Введите число '))
#     print(is_prime(user))

# def data(day, month, year):
#     if day in range(34) and month in range(13) and year in range(2024):
#         print('Правильная дата')
#         return True
#     else:
#         print("Не правильная дата")
#     return False
#
#
# while 1:
#     den = int(input('Введите день'))
#     mes = int(input('Введите месяц'))
#     god = int(input('Введите год'))
#     print(data(den, mes, god))
