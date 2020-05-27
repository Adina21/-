# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import os
from abc import ABCMeta, abstractmethod

class StatSpell(metaclass=ABCMeta):

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.sort_stat = {}

    def sorted(self):
        self.collect()
        self.sorting_stat()
        self.print()

    @abstractmethod
    def sorting_stat(self):
        pass

    def collect(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        if char in self.stat:
                            self.stat[char] += 1
                        else:
                            self.stat[char] = 1

    def print(self):
        count = 0
        print('+----------+----------+')
        print('|{txt:^10}|{t:^10}|'.format(txt='буква', t='частота'))
        print('+----------+----------+')
        for spell in self.sort_stat:
            count += self.sort_stat[spell]
            print(f'|{spell:^10}|{self.sort_stat[spell]:^10}|')
        print('+----------+----------+')
        print('|{txt:^10}|{count:^10}|'.format(txt='итого', count=count))
        print('+----------+----------+')


class StatDescending(StatSpell):

    def sorting_stat(self):
        self.sort_stat = dict(sorted(self.stat.items(), key=lambda i: i[1], reverse=True))
        return self.sort_stat  # Если метод напрямую меняет атрибут - то наверное и return особо не нужен :)


class StatAscending(StatSpell):

    def sorting_stat(self):
        self.sort_stat = dict(sorted(self.stat.items(), key=lambda i: i[1]))
        return self.sort_stat


class StatAlphabetAs(StatAscending):
    def sorting_stat(self):
        self.sort_stat = dict(sorted(self.stat.items(), key=lambda i: i[0]))
        return self.sort_stat


class StatAlphabetDes(StatAscending):
    def sorting_stat(self):
        self.sort_stat = dict(sorted(self.stat.items(), key=lambda i: i[0], reverse=True))
        return self.sort_stat

file_name = 'C:\\Users\\ASUS\\PycharmProjects\\python_base\\lesson_009\\python_snippets\\voyna-i-mir.txt'
descending =StatDescending(file_name )
descending.sorted()

ascen = StatAscending(file_name )
ascen.sorted()

alpabetas = StatAlphabetAs(file_name )
alpabetas.sorted()

alpabetdes = StatAlphabetDes(file_name )
alpabetdes.sorted()


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
#зачет!