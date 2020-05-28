# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint


ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    def __init__(self, message):
        self.message = message

    def __sizeof__(self):
        return self.message


class GluttonyError(Exception):
    def __init__(self, message):
        self.message = message

    def __sizeof__(self):
        return self.message


class DepressionError(Exception):
    def __init__(self, message):
        self.message = message

    def __sizeof__(self):
        return self.message


class SuicideError(Exception):
    def __init__(self, message):
        self.message = message

    def __sizeof__(self):
        return self.message


errors = [IamGodError('ошибка: IamGodError'),
          DrunkError('ошибка: DrunkError'),
          CarCrashError('ошибка: CarCrashError'),
          GluttonyError('ошибка: GluttonyError'),
          DepressionError('ошибка: DepressionError'),
          SuicideError('ошибка: SuicideError')]


def one_day():
    dice = randint(1, 3)
    if dice == 3:
        raise errors[randint(0, 5)]

    else:
        return randint(1, 7)


total = 0
days = 0
file = open('error.log', 'w')
while True:
    days += 1
    try:
        one_day()
        total += one_day()
    except (DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError, IamGodError) as exc:
        file.write(str(exc) + '\n')  # Добавил, чтобы лучше читалось в файле
    if total >= ENLIGHTENMENT_CARMA_LEVEL:
        print(f'Герой выбрался из временоой петли за {days} дней')
        break

file.close()
#зачет!