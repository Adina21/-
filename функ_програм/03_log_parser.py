# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

# class CheckFile():
#
#     def __init__(self, file_analysis):
#         self.file_analysis = file_analysis
#         self.count = {}
#
#
#     def calculate(self, line):
#         pass


def grouped(filename):
    group = {}
    last_time = 0
    with open(filename, 'r', encoding='utf8') as file:
        for line in file:
            if 'NOK' in line:
                group_time = line[1:17]
                if group_time not in group:
                    group[group_time] = 1
                    if last_time != 0:
                        yield last_time, group[last_time]
                    last_time = group_time
                else:
                    group[group_time] += 1
        yield group_time, group[group_time]


grouped_events = grouped(filename='events.txt')
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')

#зачет!