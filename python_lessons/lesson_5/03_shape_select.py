# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def draw_figure(point, angle, lenght, angle0, color):
    point_start = point
    for angle_step in range(0, 360 - angle0, angle0):
        vector = sd.get_vector(start_point=point, angle=angle_step + angle, length=lenght, width=3)
        vector.draw(color=color)
        point = vector.end_point
    sd.line(start_point=point, end_point=point_start, width=3, color=color)


def draw_triangle(point, angle, lenght, color):
    draw_figure(point=point, angle=angle, lenght=lenght, angle0=120, color=color)


def draw_square(point, angle, lenght, color):
    draw_figure(point=point, angle=angle, lenght=lenght, angle0=90, color=color)


def draw_pentagon(point, angle, lenght, color):
    draw_figure(point=point, angle=angle, lenght=lenght, angle0=72, color=color)


def draw_hexagon(point, angle, lenght, color):
    draw_figure(point=point, angle=angle, lenght=lenght, angle0=60, color=color)


colors = {
    '1':
        {'name': 'red', 'sd_value': sd.COLOR_RED},
    '2':
        {'name': 'orange', 'sd_value': sd.COLOR_ORANGE},
    '3':
        {'name': 'yellow', 'sd_value': sd.COLOR_YELLOW},
    '4':
        {'name': 'green', 'sd_value': sd.COLOR_GREEN},
    '5':
        {'name': 'cyan', 'sd_value': sd.COLOR_CYAN},
    '6':
        {'name': 'blue', 'sd_value': sd.COLOR_BLUE},
    '7':
        {'name': 'purple', 'sd_value': sd.COLOR_PURPLE}
}

print('Возможные цвета:')
for number, name in colors.items():
    print(number, ':', name['name'])

user_input = input('Введите желаемый цвет')
while user_input not in colors:
    print('Вы ввели не корректный номер')
    user_input = input('Введите желаемый цвет')
color_0 = colors[user_input]['sd_value']

figure = {'1': {'name': 'треугольник', 'func': draw_triangle},
          '2': {'name': 'квадрат', 'func': draw_square},
          '3': {'name': 'пятиугольник', 'func': draw_pentagon},
          '4': {'name': 'шестиугольник', 'func': draw_hexagon}
          }

print('Возможные фигуры:')
for number, name in figure.items():
    print(number, ':', name['name'])

user_input = input('Введите желаемую фигуру')
while user_input not in colors:
    print('Вы ввели не корректный номер')
    user_input = input('Введите желаемую фигуру')

functions = figure[user_input]['func']
point_0 = sd.get_point(150, 100)
functions(point=point_0, angle=0, lenght=100, color=color_0)


sd.pause()
#зачет!