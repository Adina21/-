# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

for row, y in enumerate(range(0, 600, 50)):
    for x in range(0, 600, 100):
        x0 = x + 50 if row % 2 else x
        point_start = sd.get_point(x0, y)
        point_end = sd.get_point(x0+100, y + 50)
        sd.rectangle(point_start, point_end, width=1)
sd.pause()
#зачет!