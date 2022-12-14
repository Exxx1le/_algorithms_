"""
Задание 1.
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего
Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections
Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235
Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34
Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import defaultdict

companies_num = int(input('Введите количество предприятий для расчета прибыли '))
count = 0
companies_dict = defaultdict(list)
while count != companies_num:
    company_name = input('Введите название предприятия ')
    income_for_quaters = input('Через пробел введите прибыль данного предприятия за каждый квартал (Всего 4 квартала) ')
    income_list = income_for_quaters.split(' ')
    companies_dict[company_name] = [int(i) for i in income_list]
    count += 1

overall_income_dict = defaultdict(int)
for key, val in companies_dict.items():
    overall_income_dict[key] = (sum(val))

overall_income = 0

for val in overall_income_dict.values():
    overall_income += val

average_income = overall_income / companies_num
print(f'Средняя годовая прибыль всех предприятий: {average_income}')

for key, val in overall_income_dict.items():
    if val < average_income:
        print(f'Предприятие, с прибылью ниже среднего значения: {key}, {val}')
    else:
        print(f'Предприятие, с прибылью выше среднего значения: {key}, {val}')
