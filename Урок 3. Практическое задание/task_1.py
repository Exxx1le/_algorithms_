"""
Задание 1.
Реализуйте функции:
a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
import time


def time_check(func):
    def wrapper():
        start_time = time.time()
        func()
        print("--- %s seconds ---" % (time.time() - start_time))

    return wrapper


@time_check
def list_create():
    new_list = []  # O(1)
    for i in range(1, 1000):  # O(999)
        new_list.append(i)  # O(1)
    return new_list  # O(1)


list_create()


@time_check
def dict_create():
    new_dict = {}  # O(1)
    for i in range(1, 1000):  # O(999)
        new_dict.setdefault(i, i)  # O(1)
    return new_dict  # O(1)


dict_create()


# быстрее заполняется список. Скорость заполнения словаря медленее из-за отсутствия индексов в словаре,
# а также наличии пары элементов - ключ и значение, которые нужно прописать
# в отличие от списка, который заполняется последовательно и одному индексу соответствует одно значение.

@time_check
def list_get():
    new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]  # O(1)
    for i in new_list:  # O(20)
        return i  # O(1)


list_get()


@time_check
def dict_get():
    new_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12,
                13: 13, 14: 14, 15: 15, 16: 16, 17: 17, 18: 18, 19: 19, 20: 20}  # O(1)
    for i in new_dict:  # O(20)
        return new_dict.get(i)  # O(1)


# показало одинковое время, но скорее всего словарь должен работать быстрее, потому что вызов по ключу
# не связан с поиском индекса, в отличие от списка


dict_get()


@time_check
def list_delete():
    new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]  # O(1)
    for i in new_list:  # O(20)
        new_list.pop()  # O(1)
    return new_list  # O(1)


list_delete()


@time_check
def dict_delete():
    new_dict = {1: 2, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12,
                13: 13, 14: 14, 15: 15, 16: 16, 17: 17, 18: 18, 19: 19, 20: 20}  # O(1)
    for i in new_dict.copy():  # O(20)
        new_dict.pop(i)  # O(1)
    return new_dict  # O(1)


dict_delete()

# показало одинковое время, но скорее всего словарь должен работать быстрее, потому что вызов по ключу
# не связан с поиском индекса, в отличие от списка
