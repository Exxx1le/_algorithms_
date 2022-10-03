"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""

from random import randint

number = randint(0, 100)
print(number)

count = 10

def game():
    global count
    try:
        user_number = int(input('Отгадайте число от 1 до 100 '))
        if user_number == number:
            print('Вы выйграли!')
        elif count == 0:
            print('Вы проиграли!')
        elif user_number > number:
            print('Загаданное число меньше введенного Вами')
            count -= 1
            return game()
        else:
            print('Загаданное число больше введенного Вами')
            count -= 1
            return game()
    except ValueError:
        print('Вы ввели не число')
        return game()

game()