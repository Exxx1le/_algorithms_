"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from collections import deque
from timeit import timeit

new_list = [i for i in range(1, 21)]
new_deque = deque([i for i in range(1, 21)])


# append

def append_list():
    i = 20
    while i != 0:
        new_list.append(i)
        i -= 1


def append_deque():
    i = 20
    while i != 0:
        new_deque.append(i)
        i -= 1


print(timeit("append_list()", globals=globals(), number=100))
print(timeit("append_deque()", globals=globals(), number=100))


# deque заполняется быстрее по времени, чем список

# pop

def pop_list():
    while len(new_list) != 0:
        new_list.pop()


def pop_deque():
    while len(new_deque) != 0:
        new_deque.pop()


print(timeit("pop_list()", globals=globals(), number=100))
print(timeit("pop_deque()", globals=globals(), number=100))


# список очищается быстрее по времени, чем deque

# extend

def extend_list():
    while len(new_list) != 40:
        new_list.extend(['a', 'b'])


def extend_deque():
    while len(new_deque) != 40:
        new_deque.extend(['a', 'b'])


print(timeit("extend_list()", globals=globals(), number=100))
print(timeit("extend_deque()", globals=globals(), number=100))


# decue работает быстрее списка

# leftappend

def appendleft_list():
    i = 20
    while i != 0:
        new_list.insert(0, i)
        i -= 1


def appendleft_deque():
    i = 20
    while i != 0:
        new_deque.appendleft(i)
        i -= 1


print(timeit("appendleft_list()", globals=globals(), number=100))
print(timeit("appendleft_deque()", globals=globals(), number=100))


# список заполняется медленнее deque

# popleft

def popleft_list():
    while len(new_list) != 0:
        new_list.pop(0)


def popleft_deque():
    while len(new_deque) != 0:
        new_deque.popleft()


print(timeit("popleft_list()", globals=globals(), number=100))
print(timeit("popleft_deque()", globals=globals(), number=100))


# decue удаляется быстрее списка

# extendleft

def extendleft_list():
    while len(new_list) != 40:
        for i in ['a', 'b']:
            new_list.insert(0, i)


def extendleft_deque():
    while len(new_deque) != 40:
        new_deque.extendleft(['a', 'b'])


print(timeit("extendleft_list()", globals=globals(), number=100))
print(timeit("extendleft_deque()", globals=globals(), number=100))


# decue расширяется быстрее списка

# получение элемента из decue и списка

def print_list():
    for i in new_list:
        print(i)


def print_decue():
    for i in new_deque:
        print(i)


print('печать списка', timeit("print_list()", globals=globals(), number=100))
print('печать дека', timeit("print_decue()", globals=globals(), number=100))

# список работает быстрее при извлечении элементов
