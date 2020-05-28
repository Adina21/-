# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел
from random import randint


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)

    return prime_numbers


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n):
        self.n = n
        self.prime_num = 0
        self.prime_nums = []

    def __iter__(self):
        self.prime_nums = []
        self.prime_num = 1  # Нужно было пропустить 1, чтобы она не добавилась в список :)
        # Иначе все цифры делились на неё и не проходили проверку, теперь всё работает
        return self

    def __next__(self):
        while self.prime_num < self.n:
            self.prime_num += 1
            for num in self.prime_nums:
                if self.prime_num % num == 0:
                    break
            else:
                self.prime_nums.append(self.prime_num)
                return self.prime_num
        else:
            raise StopIteration


#
# prime_number_iterator = PrimeNumbers(n=100)
# for number in prime_number_iterator:
#     print(number)


# после подтверждения части 1 преподователем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n, func):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            nums = str(number)
            if lucky_ticket(number) is True:
                nums += '- счастливый'
            if lucky_num(number) is True:
                nums += '- счастливое'
            if palindromic(number) is True:
                nums += '- палиндром'
            yield nums


# for number in prime_numbers_generator(n=10):
#     print(str(number))


def lucky_ticket(n):
    num = str(n)
    c = len(num) // 2
    start = 0
    end = 0
    for i, m in enumerate(num):
        if (i == c) and (len(num) % 2 != 0):
            continue
        if i >= c:
            end += int(m)
        else:
            start += int(m)
    return end == start


def palindromic(n):
    num = str(n)
    return num == num[::-1]


def lucky_num(n):
    lucky_nums = []
    for i in range(n + 1):
        lucky_nums.append(i)
    m = 1
    while m < n:
        if lucky_nums[m] != 0:
            j = m + m
            while j <= n:
                lucky_nums[j] = 0
                j = j + 2 * m

        m += 1
    lucky_nums = set(lucky_nums)
    lucky_nums.remove(0)
    return i in lucky_nums


# for number in prime_numbers_generator(n=1000, func=lucky_ticket):
#     print(f' счастливый билет {str(number)}  ')

# for number in prime_numbers_generator(n=100, func=lucky_num):
#     print(f' счастливое {str(number)}  ')
#

funcs = [lucky_ticket, lucky_num, palindromic]
for number in prime_numbers_generator(n=1000, func=funcs):
    print(f' {str(number)}  ')

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
#зачет!