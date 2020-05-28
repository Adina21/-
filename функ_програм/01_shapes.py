# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def draw_figure(point, length, angle):
        point_start = point
        angel_step = 0
        for _ in range(n-1):
            angel_step += angle
            vector = sd.get_vector(start_point=point, angle=angel_step, length=length, width=3)
            vector.draw()
            point = vector.end_point
        sd.line(start_point=point, end_point=point_start, width=3)

    return draw_figure


draw_triangle = get_polygon(3)
draw_triangle(point=sd.get_point(300, 200), length=100, angle=120)


draw_quadrangle = get_polygon(4)
draw_quadrangle(point=sd.get_point(500, 300), length=100, angle=90)


draw_pentagon = get_polygon(5)
draw_pentagon(point=sd.get_point(200, 400), length=100, angle=72)


sd.pause()
#зачет!