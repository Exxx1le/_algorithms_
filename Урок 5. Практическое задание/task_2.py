"""
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections
defaultdict(list)
int(, 16)
reduce
2) через ООП
вспомните про перегрузку методов
__mul__
__add__
"""
import functools
import collections


def six_numb():
    numb = collections.defaultdict(list)
    for i in range(2):
        user_num = input(f'Введите {i + 1}е шестнадцатиричное число ')
        numb[f'{i + 1}-{user_num}'] = list(user_num)
    print(numb)

    sum_calc = sum([int(''.join(i), 16) for i in numb.values()])
    print('Сумма ', list('%X' % sum_calc))

    mult_calc = functools.reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in numb.values()])
    print('Произведение', list('%X' % mult_calc))


six_numb()


# ООП

class SixNumber:
    def __int__(self, first_num, sec_num):
        self.first_num = first_num
        self.sec_num = sec_num

    def __add__(self, other):
        return list(hex(int(''.join(self.first_num), 16) + int(''.join(other.sec_num), 16)))[2:]

    def __mul__(self, other):
        return list(hex(int(''.join(self.first_num), 16) * int(''.join(other.sec_num), 16)))[2:]


user_first_num = list(input('Введите первое шестнадцатиричное число '))
user_sec_num = list(input('Введите второе шестнадцатиричное число '))

sum_calc = SixNumber(user_first_num, user_sec_num) + SixNumber(user_first_num, user_sec_num)

mult_calc = SixNumber(user_first_num, user_sec_num) * SixNumber(user_first_num, user_sec_num)

print(f'Cумма: {sum_calc}, Произведение: {mult_calc}')
