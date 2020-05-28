# -*- coding: utf-8 -*-


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные
import simple_draw as sd

N = 20

sd.resolution = (1200, 600)

point_x = []
point_y = []
list_lenght_snow = []

for _ in range(N):
    point_x.append(sd.random_number(100, 1000))
    point_y.append(sd.random_number(100, 1000))
    list_lenght_snow.append(sd.random_number(10, 100))


def snow_fall(point_x, point_y, list_lenght_snow):

    while True:
        for snow, x in enumerate(point_x):
            point = sd.get_point(point_x[snow], point_y[snow])
            sd.start_drawing()
            sd.snowflake(center=point, length=list_lenght_snow[snow], color=sd.background_color)
            point_y[snow] -= 10
            # Это отклонения вниз, а не вправо/влево
            # Для отклонений вправо/влево надо изменять координаты из point_x
            if point_y[snow] < 50:
                point_y[snow] += 600
            if snow % 2:  # Интересная идея
                # правда можно было бы записать попроще, либо используя тернарный оператор
                # либо просто sd.random_number(-10, 10)
                point_x[snow] -= sd.random_number(5, 10)
            else:
                point_x[snow] += sd.random_number(5, 10)
            point1 = sd.get_point(point_x[snow], point_y[snow])
            sd.snowflake(center=point1, length=list_lenght_snow[snow], color=sd.COLOR_WHITE)
            sd.finish_drawing()
            sd.sleep(0.01)
        if sd.user_want_exit():
            break


snow_fall(point_x=point_x, point_y=point_y, list_lenght_snow=list_lenght_snow)

sd.pause()


# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
#зачет!