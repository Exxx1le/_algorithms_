"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""

from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    a = [array.count(i) for i in array]
    max_int = max(a)
    count = array[a.index(max_int)]

    return f'Чаще всего встречается число {max_int}, ' \
           f'оно появилось в массиве {count} раз(а)'


print(func_1())
print(func_2())
print(func_3())

print(timeit("func_1()", globals=globals(), number=100))
print(timeit("func_2()", globals=globals(), number=100))
print(timeit("func_3()", globals=globals(), number=100))

# новая функция работает быстрее 2ой, но медленнее первой. Не смог придумать функцию быстрее первой.
