# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class NotNameError(Exception):
    def __init__(self, message):
        self.message = message

    def __sizeof__(self):
        return self.message


class NotEmailError(Exception):
    def __init__(self, message):
        self.message = message

    def __sizeof__(self):
        return self.message


class CheckRegist:

    def __init__(self, filename, good_file, bad_file):
        self.filename = filename
        self.good = good_file
        self.bad = bad_file

    def open_read(self):
        good_f = open(self.good, 'w', encoding='utf-8')
        bad_f = open(self.bad, 'w', encoding='utf-8')
        with open(self.filename, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    self.sort_regist(bad_f=bad_f, good_f=good_f, line=line)
                except ValueError as exc:
                    print(f'ValueError: {exc}')
                except NotNameError as exc:
                    print(f'NotNameError: {exc}')
                except NotEmailError as exc:
                    print(f'NotEmailError: {exc}')
        good_file.close()
        bad_f.close()

    def sort_regist(self, bad_f, good_f, line):
        name, email, age = line.split(' ')
        name = str(name)
        email = str(email)
        age = int(age)
        if len(line.split(' ')) != 3:
            bad_f.write(line)
            raise ValueError('НЕ присутсвуют все три поля')
        elif not name.isalpha():
            bad_f.write(line)
            raise NotNameError('поле имени содержит НЕ только буквы')
        elif ('@' and '.') not in email:
            bad_f.write(line)
            raise NotEmailError('поле емейл НЕ содержит @ и .(точку)')
        elif (10 >= age) or (age >= 99):
            bad_f.write(line)
            raise ValueError('поле возраст НЕ является числом от 10 до 99')
        else:
            good_f.write(line)


file_name = 'registrations.txt'
good_file = 'registrations_good.log'
bad_file = 'registrations_bad.log'

check = CheckRegist(file_name, good_file, bad_file)
check.open_read()
#зачет!