"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""
from collections import OrderedDict
from timeit import timeit

common_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
ordered_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])


def add_common_key():
    for i in range(1, 100):
        common_dict[i] = i


def add_ordered_key():
    for i in range(1, 100):
        ordered_dict[i] = i


print('добавление в обычный словарь', timeit("add_common_key()", globals=globals(), number=100))
print('добавление в ordered dict', timeit("add_ordered_key()", globals=globals(), number=100))


def get_common_key():
    for key, val in common_dict.items():
        return key, val


def get_ordered_key():
    for key, val in ordered_dict.items():
        return key, val


print('извлечение из обычного словаря', timeit("get_common_key()", globals=globals(), number=100))
print('извлечение из ordered dict', timeit("get_ordered_key()", globals=globals(), number=100))


def pop_common_key():
    for i in common_dict.copy():
        common_dict.pop(i)


def pop_ordered_key():
    for i in ordered_dict.copy():
        ordered_dict.pop(i)


print('удаление из обычного словаря', timeit("pop_common_key()", globals=globals(), number=100))
print('удаление из ordered dict', timeit("pop_ordered_key()", globals=globals(), number=100))

'''
во всех случаях обычный словарь работает быстрее OrderedDict. По всей видимости единственное его рабочее применение - 
это особые методы, которых нет у обычного словаря - move_to_end() и popitem()
'''
