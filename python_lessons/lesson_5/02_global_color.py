# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)1
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def draw_figure(point, angle, lenght,  angle0, color):
    point_start = point
    for angle_step in range(0, 360 - angle0, angle0):
        vector = sd.get_vector(start_point=point, angle=angle_step+angle, length=lenght, width=3)
        vector.draw(color=color)
        point = vector.end_point
    sd.line(start_point=point, end_point=point_start, width=3, color=color)


def draw_triangle(point, angle, lenght, color):
    draw_figure(point=point, angle=angle, lenght=lenght, angle0=120, color=color)


def draw_square(point, angle, lenght, color):
    draw_figure(point=point, angle=angle, lenght=lenght, angle0=90,  color=color)


def draw_pentagon(point, angle, lenght, color):
    draw_figure(point=point, angle=angle, lenght=lenght, angle0=72,  color=color)


def draw_hexagon(point, angle, lenght, color):
    draw_figure(point=point, angle=angle, lenght=lenght, angle0=60,  color=color)


colors = {
    '1':
        {'name': 'red', 'sd_value': sd.COLOR_RED},
    '2':
        {'name': 'orange', 'sd_value': sd.COLOR_ORANGE},
    '3':
        {'name': 'yellow', 'sd_value': sd.COLOR_YELLOW},
    '4':
        {'name': 'green', 'ssd_value': sd.COLOR_GREEN},
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

user_input = input('Введите желаемый цвет>')
while user_input not in colors:
    print('Вы ввели не корректный номер')
    user_input = input('Введите желаемый цвет>')

color_0 = colors[user_input]['sd_value']

point_0 = sd.get_point(150, 100)
draw_triangle(point=point_0, angle=0, lenght=100, color=color_0)

point_1 = sd.get_point(200, 250)
draw_square(point=point_1, angle=0, lenght=100, color=color_0)


point_2 = sd.get_point(100, 400)
draw_pentagon(point=point_2, angle=0, lenght=50, color=color_0)


point_3 = sd.get_point(350, 350)
draw_hexagon(point=point_3, angle=0, lenght=100, color=color_0)


sd.pause()
#зачет!