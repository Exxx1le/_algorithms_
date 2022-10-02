"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""

sum_number = 1


def sum_of_numbers(count, number=1):
    global sum_number
    if count == 1:
        return sum_number
    elif count > 1:
        number = (number / -2)
        sum_number += number
        count -= 1
        return sum_of_numbers(count, number)
    elif count <= 0:
        print('Вы ввели отрицательное число или 0')


print(sum_of_numbers(3))
