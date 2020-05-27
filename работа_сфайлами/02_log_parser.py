# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import os
import time
from pprint import pprint
from abc import ABCMeta, abstractmethod

class CheckFile(metaclass=ABCMeta):

    def __init__(self, file_analysis, file_result):
        self.file_analysis = file_analysis
        self.file_result = file_result
        self.count = {}

    @abstractmethod
    def calculate(self, line):
        pass

    def read_file(self):
        with open(self.file_analysis, 'r', encoding='utf8') as file:
            for line in file:
                if 'NOK' in line:
                    data = self.calculate(line=line)
                    if data not in self.count:
                        self.count[data] = 1
                    else:
                        self.count[data] += 1
                self.write_file()

    def write_file(self):
        with open(self.file_result, 'w', encoding='utf8') as res_file:
            for data in self.count:
                new_line = str(data) + ' ' + str(self.count[data])
                res_file.write(new_line)
                res_file.write('\n')


class CalcMin(CheckFile):
    def calculate(self, line):
        minute = line[0:17] + ']'
        return minute


class CalcHour(CheckFile):
    def calculate(self, line):
        hour = line[0:14] + ']'
        return hour


class CalcMonth(CheckFile):
    def calculate(self, line):
        month = line[0:8] + ']'
        return month


class CalcYear(CheckFile):
    def calculate(self, line):
        year = line[0:5] + ']'
        return year


calcmin = CalcMin(file_analysis='events.txt', file_result='res_min.txt')
calcmin.read_file()

calchour = CalcHour(file_analysis='events.txt', file_result='res_hour.txt')
calchour.read_file()

calcmonth = CalcMonth(file_analysis='events.txt', file_result='res_month.txt')
calcmonth.read_file()

calcyear = CalcYear(file_analysis='events.txt', file_result='res_year.txt')
calcyear.read_file()


# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
#зачет!