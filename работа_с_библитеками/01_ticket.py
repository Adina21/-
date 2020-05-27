# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
import os
import argparse
from PIL import Image, ImageDraw, ImageFont, ImageColor


def make_ticket(fio, from_, to, date, save_file):
    im = Image.open('images\\ticket_template.png')
    draw = ImageDraw.Draw(im)
    font_path = os.path.join("python_snippets\\fonts", "ofont.ru_Arial.ttf")
    font = ImageFont.truetype(font_path, size=20)
    y = im.size[1] - 280
    draw.text((50, y), fio, font=font, fill=ImageColor.colormap['black'])

    y = y + 70
    draw.text((50, y), from_, font=font, fill=ImageColor.colormap['black'])

    y = y + 65
    draw.text((50, y), to, font=font, fill=ImageColor.colormap['black'])

    x = im.size[0] - 400
    draw.text((x, y), date, font=font, fill=ImageColor.colormap['black'])
    im.save(save_file)
    print(f'image save succesful in {save_file}')


# возникшую проблему с устанвкой библиотеки на виртиулььное окружение, к сожелению не смогла решить:(
# данной программе исползован виртуальноое окружение сохраненный в проект
# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.


parser = argparse.ArgumentParser()
parser.add_argument('--fio', type=str, required=True)
parser.add_argument('--from_', type=str, required=True)
parser.add_argument('--to', type=str, required=True)
parser.add_argument('--date', type=str, required=True)
parser.add_argument('--save_to', type=str)
parser.add_argument('--make_tick', action='store_const', const=make_ticket)
args = parser.parse_args(['--make_tick', '--fio', 'Вахидова А.В', '--from_', 'Земля', '--to', 'Марс',
                          '--date', '06.03', '--save_to', 'prob.png'])
args.make_tick(args.fio, args.from_, args.to, args.date, args.save_to)
#зачет!