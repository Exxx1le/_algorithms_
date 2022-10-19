"""
Задание 2.
Попытайтесь выполнить профилирование памяти в любом скрипте с рекурсией.
Вам нужно обнаружить проблему в процессе этого. Но проблема связана не с тем,
что рекурсия потребляет много памяти, а с самим процессом замеров.
Опищите эту проблему и найдите простой путь ее решения.
Опишите этот путь и покажите его применение
"""
from memory_profiler import profile


@profile
def memory_checker():
    def get_sum():
        lst = [i for i in range(100)]
        if len(lst) == 1:
            return lst[0]
        else:
            return lst[0] + get_sum(lst[1:])


memory_checker()

"""
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    11     19.7 MiB     19.7 MiB           1   @profile
    12                                         def memory_checker():
    13     19.7 MiB      0.0 MiB           1       def get_sum():
    14                                                 lst = [i for i in range(100)]
    15                                                 if len(lst) == 1:
    16                                                     return lst[0]
    17                                                 else:
    18                                                     return lst[0] + get_sum(lst[1:])
"""

# для оценки рекурсии необходимо использовать внешнюю функцию
