# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.food = 50
        self.money = 100
        self.dirt_degree = 0
        self.cat_food = 30

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, степень грязи {}, корм для кота {} '.format(
            self.food, self.money, self.dirt_degree, self.cat_food)

    def act(self):
        self.dirt_degree += 5


class Man:

    total_food = 0

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = None

    def __str__(self):
        return '{}: степень сытости {}, степень счастья {} '.format(self.name, self.fullness, self.happiness)

    def have_home(self, house):
        self.house = house

    def eat(self):
        if self.house.food >= 50:
            self.fullness += 30
            self.house.food -= 30
            Man.total_food += 30
        else:
            self.fullness += 10
            self.house.food -= 10
            Man.total_food += 10

    def buy_cat_food(self):
        if self.house.cat_food <= 30:
            self.fullness -= 10
            self.house.money -= 30
            self.house.cat_food += 30

    def caress_cat(self):
        self.happiness += 5

    def act(self):
        if self.happiness <= 50:
            self.caress_cat()
        elif self.house.cat_food <= 10:
            self.buy_cat_food()
        if self.house.dirt_degree >= 90:
            self.happiness -= 10



class Husband(Man):

    def __init__(self, name):
        super().__init__(name=name)
        self.total_money = 0

    def act(self):
        super().act()
        if self.fullness <= 30:
            self.eat()
        elif self.house.money <= 200:
            self.work()
        elif self.house.money >= 100:
            self.gaming()

    def eat(self):
        if self.house.food >= 10:
            super().eat()

    def work(self):
        self.house.money += 150
        self.total_money += 150
        self.fullness -= 10

    def gaming(self):
        self.happiness += 20
        self.fullness -= 10


class Wife(Man):

    def __init__(self, name):
        super().__init__(name=name)
        self.total_coat = 0

    def act(self):
        super().act()
        if self.fullness <= 30:
            self.eat()
        elif self.house.money >= 350:
            self.buy_fur_coat()
        elif self.house.food <= 50:
            self.shopping()
        elif self.house.dirt_degree >= 100:
            self.clean_house()

    def eat(self):
        if self.house.food >= 10:
            super().eat()

    def shopping(self):
        if self.house.money >= 100:
            self.house.money -= 50
            self.house.food += 50
            self.fullness -= 10

    def buy_fur_coat(self):
        self.fullness -= 10
        self.house.money -= 350
        self.total_coat += 1
        self.happiness += 60

    def clean_house(self):
        self.house.dirt_degree -= 100
        self.fullness -= 10


class Cat:

    total_cat_food = 0

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.house = None

    def __str__(self):
        return '{}: степень сытости {} '.format(self.name, self.fullness)

    def have_home(self, house):
        self.house = house

    def act(self):
        if (self.fullness <= 10) and (self.house.cat_food > 0):
            self.eat()
        elif self.fullness >= 50:
            self.soil()
        elif self.fullness <= 50:
            self.sleep()

    def eat(self):
        self.fullness += 20
        self.house.cat_food -= 10
        Cat.total_cat_food += 10

    def sleep(self):
        self.fullness -= 10

    def soil(self):
        self.fullness -= 10
        self.house.dirt_degree += 5


class Child(Man):

    def act(self):
        if self.fullness <= 10:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        if self.house.food >= 30:
            self.fullness += 10
            self.house.money -= 10
            self.house.food -= 10
        elif self.house.food <= 20:
            self.fullness += 5
            self.house.money -= 5
            self.house.food -= 5

    def sleep(self):
        self.fullness -= 10


class Simulation:

    def __init__(self, money_incidents, food_incidents):
        self.money_incidents = money_incidents
        self.food_incidents = food_incidents

    def experiment(self, salary):

        House.money = salary
        home = House()
        serge = Husband(name='Сережа')
        masha = Wife(name='Маша')
        kolya = Child(name='Коля')
        serge.have_home(house=home)
        masha.have_home(house=home)
        kolya.have_home(house=home)
        cats = [Cat(name='Мурзик'),
                Cat(name='Персик'),
                Cat(name='Ричард'),
                Cat(name='Барсик'),
                Cat(name='Мурзик')
                ]
        for cat in cats:
            cat.have_home(house=home)
        for _ in range(3):
            for day in range(365):
                serge.act()
                masha.act()
                kolya.act()
                for cat in cats:
                    cat.act()
                    if cat.fullness == 0:
                        cats.remove(cat)
        return len(cats)


for food_incidents in range(6):
    for money_incidents in range(6):
        life = Simulation(money_incidents, food_incidents)
        for salary in range(50, 401, 50):
            max_cats = life.experiment(salary)
            print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
#зачет!