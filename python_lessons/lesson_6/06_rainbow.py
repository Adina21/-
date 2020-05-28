# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

point_start = sd.get_point(50, 50)
point_end = sd.get_point(350, 450)
point = sd.get_point(40, -10)


# def rainbow(point1, point2):
#     for color in rainbow_colors:
#         point_start.x += 5
#         point_end.x += 5
#         sd.line(point_start, point_end, color=color, width=4)
#
#
# rainbow(point1=point_start, point2=point_end)


def rainbows(point1, step):
    for color in rainbow_colors:
        step += 10
        sd.circle(point, radius=step, color=color, width=10)


rainbows(point1=point, step=600)


sd.pause()

# Зачет!
