# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)


def bubble(point, step, color):
    radius = 100
    color = color
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=2)


for _ in range(100):
    point1 = sd.random_point()
    step1 = random.randint(2, 10)
    color1 = sd.random_color()
    bubble(point=point1, step=step1, color=color1)
sd.pause()

#зачет!