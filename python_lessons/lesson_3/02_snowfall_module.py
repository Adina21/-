# -*- coding: utf-8 -*-

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)

  #  нарисовать_снежинки_цветом(color=sd.background_color)
    #  сдвинуть_снежинки()
    #  нарисовать_снежинки_цветом(color)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)


import simple_draw as sd
from snowfall import create_snowflakes, draw_snowflakes_color, shift_snowflakes, screen_reach_numbers, del_snowflakes

create_snowflakes(N=20)

while True:
    sd.start_drawing()
    draw_snowflakes_color(color=sd.background_color)
    shift_snowflakes()
    draw_snowflakes_color(color=sd.COLOR_WHITE)
    result_screen_reach = screen_reach_numbers()
    if result_screen_reach:
        del_snowflakes(nums=result_screen_reach)
        create_snowflakes(N=len(result_screen_reach))
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break


sd.pause()
#зачет!