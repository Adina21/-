# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


root_point = sd.get_point(500, 30)

#
# def draw_branches(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     v2 = sd.get_vector(start_point=point, angle=angle+60, length=length, width=3)
#     v2.draw()
#     return v1.end_point, v2.end_point
#
#
# angle_0 = 90
# length_0 = 200
# draw_branches(point=root_point, angle=angle_0-30, length=length_0)
# - 1 часть


# часть 2
def draw_branches(point, angle, length):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw()
    next_point = v1.end_point
    length1 = length * sd.random_number(90, 110) / 100
    angle_1 = angle + 30
    angle_2 = angle - 30
    next_angle = angle_1 * sd.random_number(90, 110) / 100
    next_angle1 = angle_2 * sd.random_number(90, 110) / 100
    next_length = length1 * .75
    draw_branches(point=next_point, angle=next_angle, length=next_length)
    draw_branches(point=next_point, angle=next_angle1, length=next_length)


draw_branches(point=root_point, angle=90, length=200)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg


# Пригодятся функции
# sd.random_number()

sd.pause()
#зачет!