"""Функция используется во views.py"""
import re


def format_version(string):
    """Для валидации формата версии справочника от 0.0.0 до 99.99.99."""
    while True:
        if re.match(r'^[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{1,2}$', string):
            return string
        print(
            'Некорректный формат версии. '
            'Введите версию в формате:'
            '`1.0.0`, `0.2.0`, `05.0.9`, `01.22.34`'
        )
