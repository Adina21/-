#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['дедушка', 'бабушка', 'мама']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['дедушка', 170],
    ['бабушка', 156],
    ['мама', 167],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('рост дедушки',my_family_height[0][1],'см')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
general = my_family_height[0][1]+my_family_height[1][1]+my_family_height[2][1]
#   Общий рост моей семьи - ХХ см
print('общий рост моей семььи',general,'см')

# Зачет!