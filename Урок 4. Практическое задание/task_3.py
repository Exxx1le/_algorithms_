"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def my_revers(num):
    return ''.join(list(reversed(str(num))))


print(timeit("revers(6655321)", globals=globals(), number=100))
print(timeit("revers_2(6655321)", globals=globals(), number=100))
print(timeit("revers_3(6655321)", globals=globals(), number=100))
print(timeit("my_revers(6655321)", globals=globals(), number=100))

"""
Наиболее быстрый вариант revers_2. Он быстрее 3 и 4 варианта, потому что нет этапа преобразования числа в строку, а 
также создания списка. Также этот вариант оказался быстрее рекурсии из первой функции, поскольку решение получается в 
рамках одного цикла без развилки else if, которая присутствует в рекурсии. Эта развилка требует проверки входящих 
в функцию параметров при каждом рекурсивном запуске функции.
"""
