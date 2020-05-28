# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.point_x = sd.random_number(100, 1000)
        self.point_y = sd.random_number(100, 1000)
        self.list_lenght = sd.random_number(10, 100)

    def draw(self):
        point = sd.get_point(self.point_x, self.point_y)
        sd.snowflake(center=point, length=self.list_lenght, color=sd.COLOR_WHITE)

    def move(self):
        if self.point_y > 50:
            self.point_y -= 10
        else:
            self.point_y = 50
        self.point_x += sd.random_number(-10, 10)

    def can_fall(self):
        return self.point_y > 50

    def clear_previous_picture(self):
        point = sd.get_point(self.point_x, self.point_y)
        sd.snowflake(center=point, length=self.list_lenght, color=sd.background_color)



# flake = Snowflake()


# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:


def get_flakes(count):
    snowflake = []
    for _ in range(count):
        snowflake.append(Snowflake())
    return snowflake


def get_fallen_flakes():
    fall_flakes = []
    for index, flake in enumerate(flakes):
        if not flake.can_fall():
            fall_flakes.append(index)
    for flk in reversed(fall_flakes):
        flakes.pop(flk)
    return fall_flakes


def append_flakes(count):
    for _ in range(count):
        flakes.append(Snowflake())


N = 10
flakes = get_flakes(count=N)
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = len(get_fallen_flakes())
    if fallen_flakes:
        append_flakes(count=fallen_flakes)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
#зачет!