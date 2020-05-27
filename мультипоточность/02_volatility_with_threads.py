# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.

# -*- coding: utf-8 -*-

import os
from pprint import pprint
import threading


class Tickers(threading.Thread):
    def __init__(self, file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file = file
        self.tick_volatility = None

    def run(self):
        with open(self.file, 'r') as f:
            list_price = []
            for i, line in enumerate(f):
                if i == 0:
                    continue
                secid, tradetime, price, quantity = line.split(',')
                list_price.append(float(price))
            self.tick_volatility = (secid, self.calc(list_price))
            return self.tick_volatility

    def calc(self, list_price):
        mx = max(list_price)
        mn = min(list_price)
        average_price = (mx + mn) / 2
        volatility = ((mx - mn) / average_price) * 100
        return volatility


def file_path_generator(path):
    norm_path = os.path.normpath(path)
    for dirpath, dirname, filenames in os.walk(norm_path):
        for file in filenames:
            full_file_path = os.path.join(dirpath, file)
            yield full_file_path


def print_result(res):
    min_max = []
    zero = []
    sort_res = sorted(res, key=lambda i: (-i[1], i[0]))
    for tick_name, volatility in sort_res:
        index = sort_res.index((tick_name, volatility))
        if volatility == 0:
            min_max = sort_res[:index]
            zero = sort_res[index:]
            break
    print('Максимальная волатильность:')
    pprint(min_max[:3])
    print('Минимальная волатильность:')
    pprint(min_max[-3:])
    print('Нулевая волатильность:')
    pprint(zero)

res = []
tickers = [Tickers(file=file) for file in file_path_generator('trades')]
for ticker in tickers:
    ticker.start()
for ticker in tickers:
    ticker.join()
for ticker in tickers:
    res.append(ticker.tick_volatility)

print_result(res)
#зачет!