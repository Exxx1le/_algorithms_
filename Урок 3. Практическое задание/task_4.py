"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет
Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}
Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

import hashlib


def dict_url(url, dictionary):
    if dictionary.get(url) is not None:
        return dictionary.get(url)
    else:
        hash_obj = hashlib.pbkdf2_hmac(hash_name='sha256',
                                       password=url.encode(encoding="utf-8"),
                                       salt=b'my_salt_1',
                                       iterations=1000)
        return dictionary.setdefault(url, str(hash_obj))


url_dict = {}

dict_url('www.rambler.ru', url_dict)
print(url_dict)
print(dict_url('www.rambler.ru', url_dict))
