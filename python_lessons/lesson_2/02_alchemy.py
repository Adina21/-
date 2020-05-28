# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:

    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm(elem1=self, elem2=other)
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud(elem1=self, elem2=other)
        else:
            return None


class Air:

    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm(elem1=self, elem2=other)
        elif isinstance(other, Fire):
            return Lightning(elem1=self, elem2=other)
        elif isinstance(other, Earth):
            return Dust(elem1=self, elem2=other)
        elif isinstance(other, Steam):
            return Cloud()
        else:
            return None


class Fire:
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning(elem1=self, elem2=other)
        elif isinstance(other, Earth):
            return Lava(elem1=self, elem2=other)
        else:
            return None


class Earth:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Mud(elem1=self, elem2=other)
        elif isinstance(other, Air):
            return Dust(elem1=self, elem2=other)
        elif isinstance(other, Fire):
            return Lava(elem1=self, elem2=other)
        else:
            return None


class Storm:
    def __init__(self, elem1, elem2):
        self.elem1 = elem1
        self.elem2 = elem2

    def __str__(self):
        return 'Шторм = ' + str(self.elem1) + ' + ' + str(self.elem2)


class Steam:

    def __str__(self):
        return 'Пар  '

    def __add__(self, other):
        if isinstance(other, Air):
            return Cloud()


class Mud:
    def __init__(self, elem1, elem2):
        self.elem1 = elem1
        self.elem2 = elem2

    def __str__(self, ):
        return 'Грязь = ' + str(self.elem1) + ' + ' + str(self.elem2)


class Lightning:
    def __init__(self, elem1, elem2):
        self.elem1 = elem1
        self.elem2 = elem2

    def __str__(self):
        return 'Молния = ' + str(self.elem1) + ' + ' + str(self.elem2)


class Dust:
    def __init__(self, elem1, elem2):
        self.elem1 = elem1
        self.elem2 = elem2

    def __str__(self):
        return 'Пыль = ' + str(self.elem1) + ' + ' + str(self.elem2)


class Lava:
    def __init__(self, elem1, elem2):
        self.elem1 = elem1
        self.elem2 = elem2

    def __str__(self):
        return 'Лава = ' + str(self.elem1) + ' + ' + str(self.elem2)


class Cloud:
    def __str__(self):
        return 'Облака'


# print(Water(), '+', Air(), '=', Water() + Air())
# print(Water(), '+', Fire(), '=', Water() + Fire())
# print(Water(), '+', Earth(), '=', Earth() + Water())
# print(Air(), '+', Earth(), '=', Earth() + Air())
#print(Fire(), '+', Earth(), '=', Fire() + Earth())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
# Подскажите, пожалуйста, способ  определение результата функции  _add_ без атрибуьов
print(Steam(), '+', Air(), '=', Steam(), '+', Air())
#зачет!