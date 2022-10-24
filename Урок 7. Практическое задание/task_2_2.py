"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
2) без сортировки
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from timeit import timeit
from random import randint


def nosort(lst):
    new_list = lst
    for i in range(len(lst) // 2):
        new_list.remove(max(new_list))
    return max(new_list)


m = 100
my_list = [randint(0, 100) for i in range(2 * m + 1)]

print(timeit('nosort(my_list[:])', globals=globals(), number=100))

# 0.03000069997506216
