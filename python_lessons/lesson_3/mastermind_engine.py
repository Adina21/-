
import random

_guessed_num = 0


def make_number():
    global _guessed_num
    num = []
    for i in range(1000, 10000):
        s = str(i)
        if len(set(map(int, s))) == 4:
            num.append(list(map(int, s)))
    _guessed_num = random.choice(num)


def check_number(us_nums):

    cows, bulls = 0, 0
    for i, nums in enumerate(us_nums):
        if nums in _guessed_num:
            if us_nums[i] == _guessed_num[i]:
                bulls += 1
            else:
                cows += 1
    return {'быки': bulls,
            'коровы': cows}


