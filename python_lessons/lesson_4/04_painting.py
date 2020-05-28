# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)


import simple_draw as sd

from painting.rainbow import rainbows, point

from painting.smile import smile

from painting.tree import draw_branches, root_point, root_point1, root_point2

from painting.snowflake import *

from painting.house import paint_house, point_list, point_list1

from painting.walls import paint_walls

from painting.sun import paint_sun, centre_point

#
sd.resolution = (1200, 600)


while True:
    sd.clear_screen()
    paint_walls(x1=250, x2=500, y1=30, y2=255, count=2)
    paint_house(point_list=point_list, point_list1=point_list1)
    rainbows(point1=point, step=800, count=2)
    paint_sun(point=centre_point, angle=sd.random_number(0, 360), lenght=90)
    snow_fall(point_x=point_x, point_y=point_y, list_lenght_snow=list_lenght_snow)
    smile(x=600, y=240, color=sd.COLOR_ORANGE)
    draw_branches(point=root_point, angle=90, length=70)

    draw_branches(point=root_point1, angle=90, length=40)

    draw_branches(point=root_point2, angle=90, length=40)
    sd.sleep(0.1)
    sd.finish_drawing()
    if sd.user_want_exit():
        break


sd.pause()
# Давайте попробуем начать вот с чего. Сделайте два кадра
# Просто два статичных изображения, на одном лучи солнца в одном месте, на другом - в другом
# И добавьте разный порядок цветов в радуге

# Попробуйте вот такой приём - создайте в функции ещё один параметр, если он равен 1
# то солнце рисуется в одной позиции (без анимации)
# Если же параметр равен 2 - солнце рисуется в другой позиции
# Теперь попробуйте в цикле менять эти два кадра
# 1ый кадр - очистка экрана - 2ой кадр... и тд
# поэксперементировала с анимацией, лучи солнце сдвиг угла
# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.
#зачет!