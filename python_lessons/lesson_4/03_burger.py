# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  -булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

# TODO Здесь можно перечислить функции через запятую
from my_burger import add_cucumber

from my_burger import add_cutlets

from my_burger import add_onion

from my_burger import add_cheese

from my_burger import add_ketchup

from my_burger import add_buns

double_cheese_burger = {
    '1': {'func': add_buns},
    '2': {'func': add_cutlets},
    '3': {'func': add_cheese},
    '4': {'func': add_ketchup},
    '5': {'func': add_onion},
    '6': {'func': add_cucumber}
}

for number, func in double_cheese_burger.items():
    print(number)
    functions = double_cheese_burger[number]['func']
    functions()

# чтобы  с помощью этих же фунций смогли составить разные рацепты бурргеров использовала словарь
# (только с выводом немножко не понятно :) )как сделать
# вывод словаря так, чтобя  выглядел приа=мерно так : 1. Булочку разрежем пополам  и начинаем собирать чизбургер
# 2 Булочку разрежем пополам  и начинаем собирать чизбургер.... и тд.

# подскажите, пожалуйста, как сделать  вывод, чтобы  при выводе номер и функция в одну строчку
#зачет!