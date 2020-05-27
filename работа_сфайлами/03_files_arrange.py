# -*- coding: utf-8 -*-

import os, time, shutil, zipfile
from abc import ABCMeta, abstractmethod


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class SortFile(metaclass=ABCMeta):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def sorted_file(self):
        pass


class SortZipFile(SortFile):

    def sorted_file(self):
        zfile = zipfile.ZipFile(self.path, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
            path_normalzed = os.path.normpath(filename)
            for dirpath, dirnames, filenames in os.walk(path_normalzed):
                for file in filenames:
                    print(file)
                    full_file_path = os.path.join(dirpath, file)
                    secs = os.path.getmtime(full_file_path)
                    file_time = time.gmtime(secs)
                    new_path = r'icons_by_year'
                    name_file = '\\' + str(file_time[0]) + '\\' + str(file_time[1])
                    new_path += os.path.normpath(name_file)
                    os.makedirs(new_path, exist_ok=True)
                    shutil.copy2(full_file_path, new_path)


class SortUnzipFile(SortFile):
    def sorted_file(self):
        path_normalzed = os.path.normpath(self.path)
        for dirpath, dirnames, filenames in os.walk(path_normalzed):
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                secs = os.path.getmtime(full_file_path)
                file_time = time.gmtime(secs)
                new_path = r'icons_by_year'
                name_file = '\\' + str(file_time[0]) + '\\' + str(file_time[1])
                new_path += os.path.normpath(name_file)
                os.makedirs(new_path, exist_ok=True)
                shutil.copy2(full_file_path, new_path)


# sortzipfile = SortZipFile('icons.zip')
# sortzipfile.sorted_file()

sortfile = SortUnzipFile('icons')
sortfile.sorted_file()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
#зачет!