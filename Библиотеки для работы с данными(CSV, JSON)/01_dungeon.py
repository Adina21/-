# -*- coding: utf-8 -*-

# Подземелье было выкопано ящеро-подобными монстрами рядом с аномальной рекой, постоянно выходящей из берегов.
# Из-за этого подземелье регулярно затапливается, монстры выживают, но не герои, рискнувшие спуститься к ним в поисках
# приключений.
# Почуяв безнаказанность, ящеры начали совершать набеги на ближайшие деревни. На защиту всех деревень не хватило
# солдат и вас, как известного в этих краях героя, наняли для их спасения.
#
# Карта подземелья представляет собой json-файл под названием rpg.json. Каждая локация в лабиринте описывается объектом,
# в котором находится единственный ключ с названием, соответствующем формату "Location_<N>_tm<T>",
# где N - это номер локации (целое число), а T (вещественное число) - это время,
# которое необходимо для перехода в эту локацию. Например, если игрок заходит в локацию "Location_8_tm30000",
# то он тратит на это 30000 секунд.
# По данному ключу находится список, который содержит в себе строки с описанием монстров а также другие локации.
# Описание монстра представляет собой строку в формате "Mob_exp<K>_tm<M>", где K (целое число) - это количество опыта,
# которое получает игрок, уничтожив данного монстра, а M (вещественное число) - это время,
# которое потратит игрок для уничтожения данного монстра.
# Например, уничтожив монстра "Boss_exp10_tm20", игрок потратит 20 секунд и получит 10 единиц опыта.
# Гарантируется, что в начале пути будет две локации и один монстр
# (то есть в коренном json-объекте содержится список, содержащий два json-объекта, одного монстра и ничего больше).
#
# На прохождение игры игроку дается 123456.0987654321 секунд.
# Цель игры: за отведенное время найти выход ("Hatch")
#
# По мере прохождения вглубь подземелья, оно начинает затапливаться, поэтому
# в каждую локацию можно попасть только один раз,
# и выйти из нее нельзя (то есть двигаться можно только вперед).
#
# Чтобы открыть люк ("Hatch") и выбраться через него на поверхность, нужно иметь не менее 280 очков опыта.
# Если до открытия люка время заканчивается - герой задыхается и умирает, воскрешаясь перед входом в подземелье,
# готовый к следующей попытке (игра начинается заново).
#
# Гарантируется, что искомый путь только один, и будьте аккуратны в рассчетах!
# При неправильном использовании библиотеки decimal человек, играющий с вашим скриптом рискует никогда не найти путь.
#
# Также, при каждом ходе игрока ваш скрипт должен запоминать следущую информацию:
# - текущую локацию
# - текущее количество опыта
# - текущие дату и время (для этого используйте библиотеку datetime)
# После успешного или неуспешного завершения игры вам необходимо записать
# всю собранную информацию в csv файл dungeon.csv.
# Названия столбцов для csv файла: current_location, current_experience, current_date
#
#
# Пример взаимодействия с игроком:
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло времени: 00:00
#
# Внутри вы видите:
# — Вход в локацию: Location_1_tm1040
# — Вход в локацию: Location_2_tm123456
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали переход в локацию Location_2_tm1234567890
#
# Вы находитесь в Location_2_tm1234567890
# У вас 0 опыта и осталось 0.0987654321 секунд до наводнения
# Прошло времени: 20:00
#
# Внутри вы видите:
# — Монстра Mob_exp10_tm10
# — Вход в локацию: Location_3_tm55500
# — Вход в локацию: Location_4_tm66600
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали сражаться с монстром
#
# Вы находитесь в Location_2_tm0
# У вас 10 опыта и осталось -9.9012345679 секунд до наводнения
#
# Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!
#
# У вас темнеет в глазах... прощай, принцесса...
# Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)
# Ну, на этот-то раз у вас все получится! Трепещите, монстры!
# Вы осторожно входите в пещеру... (текст умирания/воскрешения можно придумать свой ;)
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло уже 0:00:00
# Внутри вы видите:
#  ...
#  ...
#
# и так далее...
import csv
from datetime import datetime
import json
import re
from decimal import Decimal

remaining_time = '123456.0987654321'
re_time = r'_tm((\d+)|(.\d+)|0)'
re_mons_exp = r'_exp(\d+)'


class Map:
    def __init__(self, json_file, re_time):
        self.re_time = re_time
        self.json_file = json_file
        self.current_location = {}
        self.actual_monsters = {}
        self.actual_locations = {}
        self.list_act_mons = []
        self.location_time = 0

    def download_file(self):
        with open(self.json_file, 'r') as file_with_data:
            self.current_location = json.load(file_with_data)
        return self.current_location

    def analysis_location(self):
        print('-' * 30)
        for key, value in self.current_location.items():
            if key == 'Hatch_tm159.098765432':
                break
            print(key)
            print(f'Вы находитесь в {key}')
            print('Внутри вы видите:')
            for index, element in enumerate(value):
                if 'Mob' in element or 'Boss' in element:
                    if element not in self.actual_monsters:
                        print(f'— {index + 1} Монстра {element}')
                        self.actual_monsters[index] = element
                        self.list_act_mons.append(element)
                else:
                    for location in element:
                        print(f'— {index + 1} Вход в локацию: {location}')
                        if location not in self.actual_locations:
                            self.actual_locations[index + 1] = location

    def change_location(self):
        for key, value in self.current_location.items():
            if self.actual_locations == {}:
                print('Нет доступеных локации'
                      ' Вы можете выбрать действие "Атаковать монстра", или выход из игры')
                self.location_time = 0
            elif len(self.actual_locations) > 1:
                print('-' * 30)
                print('Доступные локации:')
                for index, name in self.actual_locations.items():
                    print(f'- №{index} {name}')
                gamer_location = input('Выберите номер локацию:')
                while int(gamer_location) not in self.actual_locations.keys():
                    print('Ввели неккоректный формат!'
                          'Номер локации должен быть целым числом,укажите только доступные номера локации')
                    gamer_location = input('Выберите номер локацию:')
                    continue
                else:
                    print(f'Вы выбрали переход в локацию  {self.actual_locations[int(gamer_location)]}')
                    self.current_location = value[int(gamer_location) - 1]
                    num_loc = int(gamer_location)
                    loc_time = re.search(self.re_time, self.actual_locations[num_loc])[1]
                    self.location_time = Decimal(loc_time)
            else:
                for index in self.actual_locations:
                    print(f'Вы выбрали переход в локацию  {self.actual_locations[index]}')
                    self.current_location = value[index - 1]
                    loc_time = re.search(self.re_time, self.actual_locations[index])[1]
                    self.location_time = Decimal(loc_time)
            self.actual_locations.clear()
            self.actual_monsters.clear()
            self.list_act_mons.clear()
        self.analysis_location()
        return self.location_time


class Hero:
    def __init__(self, re_mons_exp, re_time, actual_monsters, list_act_mons):
        self.re_mons_exp = re_mons_exp
        self.re_time = re_time
        self.delete_mons = actual_monsters
        self.mons = list_act_mons
        self.exp = 0
        self.mons_time = 0

    def attack_monster(self):
        print(self.mons)
        if len(self.delete_mons) == 0:
            print('список доступных монстров пуст.'
                  ' Выберите переход в другую локацию, или выход из игры')
            self.mons_time = 0
        else:
            for index, name in enumerate(self.mons):
                print(f' - {index + 1} {name}')
            gamer_mons = input('Выберите монстра:')
            num = int(gamer_mons) - 1
            if num in self.delete_mons.keys():
                mons_exp = re.search(self.re_mons_exp, self.delete_mons[num])[1]
                mons_time = re.search(self.re_time, self.delete_mons[num])[1]
                self.mons_time = int(mons_time)
                self.exp += int(mons_exp)
                print(f' уничтожен монстр {self.delete_mons[num]}')
                self.delete_mons.pop(num)
                print(self.delete_mons)
                print(self.mons)
            else:
                print('Ввели неккоректный формат, или возможго ранее уничтожили этот монстр!'
                      'Номер монстра должен быть целым числом больше 0, укажите только доступные номера'
                      'Нельзя указывать номер ранее уничтоженного монстра')
        return self.exp, self.mons_time, self.delete_mons


class Game:

    def __init__(self, remaining_time, re_time, re_mons_exp):
        self.re_time = re_time
        self.re_mons_exp = re_mons_exp
        self.remaining_time = Decimal(remaining_time)
        self.map = Map('rpg.json', re_time)
        self.hero = Hero(self.re_mons_exp, self.re_time, self.map.actual_monsters, self.map.list_act_mons)
        self.current_time = 0
        self.switch = True
        self.current_loc = []
        self.current_time = []
        self.current_exp = []
        self.operations = {'1': {'act': 'Атаковать монстра', 'func': self.hero.attack_monster},
                           '2': {'act': 'Перейти в другую локацию', 'func': self.map.change_location},
                           '3': {'act': 'Сдаться и выйти из игры', 'func': self.game_over},
                           }

    def game_over(self):
        print('Выход из игры ')
        self.switch = False
        return self.switch

    def account_time(self, current_time):
        self.remaining_time -= Decimal(current_time)
        return self.remaining_time

    def choose_methods(self):
        print('-' * 30)
        print('Выберите действие:')
        for number, operation in self.operations.items():
            print(number, operation['act'])
        gamer_input = input('Введите номер действие: ')
        while gamer_input not in self.operations.keys():
            print('Ввели неккоректный формат!'
                  'Номер для выобора действий, всегда меняется в диапозоне [1..3]')
            gamer_input = input('Введите номер действие: ')
            continue
        else:
            functions = self.operations[gamer_input]['func']
            functions()
        if gamer_input == '1':
            self.account_time(current_time=self.hero.mons_time)
        elif gamer_input == '2':
            self.account_time(current_time=self.map.location_time)
            for location in self.map.current_location:
                self.current_loc.append(location)
            self.current_time.append(self.remaining_time)
            self.current_exp.append(self.hero.exp)

    def write_result_game_csv(self, current_location, hero_exp, remaining_time):
        result = [{'current_location': current_location,
                   'current_experience': hero_exp,
                   'current_date': remaining_time}
                  ]

        name = [['current_location', 'current_experience', 'current_date']]
        with open('dungeon.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=name[0])
            writer.writeheader()
            writer.writerows(result)

    def run(self):
        self.map.download_file()
        self.map.analysis_location()
        while self.switch is True:
            print(f'У вас {self.hero.exp} опыта и осталось {self.remaining_time} секунд до наводнения')
            self.choose_methods()
            self.write_result_game_csv(self.current_loc, self.current_exp, self.current_time)
            if self.remaining_time <= 0:
                print('Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!')
                self.switch = False
            for name_loc, loc_element in self.map.current_location.items():
                if name_loc == 'Hatch_tm159.098765432' and self.hero.exp >= 200 and self.remaining_time > 0:
                    print('Вы победитель !!!')
                    self.switch = False


g = Game(remaining_time, re_time, re_mons_exp)
g.run()
#зачёт!