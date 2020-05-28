# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd


def smile(x, y, color):
    rad = 50
    radius = 10
    point = sd.get_point(x, y)
    point2 = sd.get_point(x-20, y+20)
    point3 = sd.get_point(x + 25, y + 20)
    point4 = sd.get_point(x-10, y-25)
    point5 = sd.get_point(x + 10, y-25)
    point6 = sd.get_point(x - 20, y - 20)
    point7 = sd.get_point(x + 22, y - 20)
    sd.circle(center_position=point, radius=rad, color=color,  width=1)
    sd.circle(center_position=point2, radius=radius, color=color, width=1)
    sd.circle(center_position=point3, radius=radius, color=color, width=1)
    sd.line(start_point=point4, end_point=point5, color=color, width=1)
    sd.line(start_point=point4, end_point=point6, color=color, width=1)
    sd.line(start_point=point5, end_point=point7, color=color, width=1)


for _ in range(10):
    x1 = sd.random_number(10, 500)
    y1 = sd.random_number(10, 500)
    color1 = sd.random_color()
    smile(x=x1, y=y1, color=color1)

sd.pause()

#зачет!