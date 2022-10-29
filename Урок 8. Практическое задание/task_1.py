"""
Задание 1.
Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""

from collections import Counter, deque


class MyClass:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def tree(s):

    count = Counter(s)

    sorted_string = deque(sorted(count.items(), key=lambda item: item[1]))

    while len(sorted_string) > 1:

        weight = sorted_string[0][1] + sorted_string[1][1]
        knot = MyClass(left=sorted_string.popleft()[0], right=sorted_string.popleft()[0])

        for i, item in enumerate(sorted_string):
            if weight > item[1]:
                continue
            else:
                sorted_string.insert(i, (knot, weight))
                break
        else:
            sorted_string.append((knot, weight))

    return sorted_string[0][0]


code_table = dict()


def code(tree, path=''):

    if not isinstance(tree, MyClass):
        code_table[tree] = path

    else:
        code(tree.left, path=f'{path}0')
        code(tree.right, path=f'{path}1')


s = "hello world!"

code(tree(s))

for i in s:
    print(code_table[i], end=' ')

print()
