"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

my_list = [12, 14, 8, 45, 2]


# 1
def list_min_complex(list_name):  # O(N^2)
    min_num = list_name[0]  # O(1)
    new_list = []
    for i in list_name[1:]:  # O(N^2) + O[b-1]
        if i < min_num:
            new_list.append(i)   # O(1)
            for j in new_list:
                min_num = new_list[0]  # O(1)
                if j < min_num:
                    min_num = j
    return new_list[-1]  # O(1)


list_min_complex(my_list)


# 2
def list_min_simple(list_name):  # O(N)
    min_num = list_name[0]  # O(1)
    for i in list_name[1:]:  # O(N) + O[b-1]
        if i < min_num:
            min_num = i  # O(1)

    return (min_num)  # O(1)


list_min_simple(my_list)
