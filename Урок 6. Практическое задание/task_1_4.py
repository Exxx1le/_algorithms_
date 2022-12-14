"""
Задание 1.
Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы Python
На каждый скрипт нужно два решения - исходное и оптимизированное.
Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler
Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler
Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.
ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.
Это файл для четвертого скрипта
"""
from collections import namedtuple
from memory_profiler import profile


# исходная функция (задание 3 к уроку 3 основ)
@profile
def thesaurus(name):
    letter_dict = {
        "И": ["Иван", "Илья"],
        "К": ["Кирилл", "Константин"],
        "Л": ["Леонид", "Лев"],
        "М": ["Мария"],
        "П": ["Петр"]
    }
    for k, v in letter_dict.items():
        for i in v:
            if i == name:
                return {k: v}


thesaurus("Леонид")

'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    29     19.9 MiB     19.9 MiB           1   @profile
    30                                         def thesaurus(name):
    31     19.9 MiB      0.0 MiB           1       letter_dict = {
    32     19.9 MiB      0.0 MiB           1           "И": ["Иван", "Илья"],
    33     19.9 MiB      0.0 MiB           1           "К": ["Кирилл", "Константин"],
    34     19.9 MiB      0.0 MiB           1           "Л": ["Леонид", "Лев"],
    35     19.9 MiB      0.0 MiB           1           "М": ["Мария"],
    36     19.9 MiB      0.0 MiB           1           "П": ["Петр"]
    37                                             }
    38     19.9 MiB      0.0 MiB           3       for k, v in letter_dict.items():
    39     19.9 MiB      0.0 MiB           7           for i in v:
    40     19.9 MiB      0.0 MiB           5               if i == name:
    41     19.9 MiB      0.0 MiB           1                   return {k: v}
'''


# производная функция
@profile
def thesaurus_2(name):
    letter_tuple = namedtuple('Names', 'И К Л М П')
    a = letter_tuple(И=["Иван", "Илья"], К=["Кирилл", "Константин"], Л=["Леонид", "Лев"], М=["Мария"], П=["Петр"])

    for i in a:
        if name in i:
            return i


thesaurus_2('Леонид')

'''
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    47     19.9 MiB     19.9 MiB           1   @profile
    48                                         def thesaurus_2(name):
    49     19.9 MiB      0.0 MiB           1       letter_tuple = namedtuple('Names', 'И К Л М П')
    50     19.9 MiB      0.0 MiB           1       a = letter_tuple(И=["Иван", "Илья"], К=["Кирилл", "Константин"], Л=["Леонид", "Лев"], М=["Мария"], П=["Петр"])
    51                                         
    52     19.9 MiB      0.0 MiB           3       for i in a:
    53     19.9 MiB      0.0 MiB           3           if name in i:
    54     19.9 MiB      0.0 MiB           1               return i

'''

# разницы в профилировании не видно, но сам по себе namedtuple должен занимать меньше памяти.
# не смог использовать recordclass из-за ошибки в установке. Также не устновился pympler.
