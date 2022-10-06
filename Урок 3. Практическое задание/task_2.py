# Задание 2.
# Ваша программа должна запрашивать пароль
# Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
# Для генерации хеша обязательно нужно использовать криптографическую соль
# Обязательно выведите созданный хеш
# Далее программа должна запросить пароль повторно и вновь вычислить хеш
# Вам нужно проверить, совпадает ли пароль с исходным
# Для проверки необходимо сравнить хеши паролей
# ПРИМЕР:
# Введите пароль: 123
# В базе данных хранится строка: 555a3581d37993843efd4eba1921
# f1dcaeeafeb855965535d77c55782349444b
# Введите пароль еще раз для проверки: 123
# Вы ввели правильный пароль
# Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
# или, если вы уже знаете, как Python взаимодействует с базами данных,
# воспользуйтесь базой данный sqlite, postgres и т.д.
# п.с. статья на Хабре - python db-api

import hashlib


def password():
    user_input = input('Введите пароль ')
    hash_obj = hashlib.pbkdf2_hmac(hash_name='sha256',
                                   password=user_input.encode(encoding="utf-8"),
                                   salt=b'my_salt_1',
                                   iterations=1000)

    print(hash_obj)

    with open('pass.csv', 'w', encoding='utf-8') as f:
        f.write(str(hash_obj))

    with open('pass.csv', 'r', encoding='utf-8') as f:
        user_input = input('Введите пароль еще раз для проверки ')
        hash_obj_2 = hashlib.pbkdf2_hmac(hash_name='sha256',
                                         password=user_input.encode(encoding="utf-8"),
                                         salt=b'my_salt_1',
                                         iterations=1000)
        print(hash_obj_2)

        if f.readlines()[0] == str(hash_obj_2):
            print('Пароль верный')
        else:
            print('Пароль неверный')


password()
