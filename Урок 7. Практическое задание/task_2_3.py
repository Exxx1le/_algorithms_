"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
3) с помощью встроенной функции поиска медианы
сделайте замеры на массивах длиной 10, 100, 1000 элементов
В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
from timeit import timeit
from random import randint
from statistics import median


def list_median(lst):
    return median(lst)


m = 100
my_list = [randint(0, 100) for i in range(2 * m + 1)]

print(timeit('list_median(my_list[:])', globals=globals(), number=100))

# 0.0009296999778598547 - самый быстрый результат
