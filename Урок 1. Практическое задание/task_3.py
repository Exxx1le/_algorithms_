"""
Задание 3.
Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

companies_income_dict = {'Microsoft': 345788798748, 'Apple': 50088798748, 'Amazon': 400788798748,
                         'Рога и копыта': 450343}


# 1

def find_top3(dictionary):  # O(N log N)

    income = []  # O(1)

    for val in dictionary.values():  # O(N)
        income.append(val)  # O(1)

    top_list = sorted(income, reverse=True)[0:3]  # O(N log N)

    top_dict = {}  # O(1)

    for k, v in dictionary.items():  # O(N^2)
        for i in top_list:  # O(N)
            if v == i:
                top_dict.setdefault(k, v)  # O(1)

    return (top_dict)  # O(1)


# 2

def find_top3_2(dictionary):  # O(N^2) данное решение лучше из-за отсутствия sorted и reverse
    income = []  # O(1)
    for keys, val in dictionary.items():  # O(N)
        income.append(val)  # O(1)

    top3 = []  # O(1)
    while len(top3) != 3:
        top3.append(max(income))  # O(1) + O(N)
        income.remove(max(income))  # O(N) + O(N)

    top_dict = {}  # O(1)

    for k, v in dictionary.items():  # O(N^2)
        for i in top3:  # O(N)
            if v == i:
                top_dict.setdefault(k, v)  # O(1)

    return (top_dict)  # O(1)


find_top3_2(companies_income_dict)
