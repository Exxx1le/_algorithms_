"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв
Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.
Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.
Пример:
рара - 6 уникальных подстрок
рар
ра
ар
ара
р
а
"""
import hashlib


def str_hash(string):
    all_set = set()
    start = 0
    while start != len(string):
        end = len(string)
        for i in string[start:end]:
            while end != start:
                new_string = string[start:end]
                hash_obj = hashlib.sha256(new_string.encode(encoding="utf-8"))
                all_set.add(hash_obj.hexdigest())
                end -= 1
        start += 1

    print(all_set)


str_hash('hello')
