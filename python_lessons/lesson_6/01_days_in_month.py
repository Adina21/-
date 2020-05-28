# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом6

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)
days = [28, 30, 31]

#user_input1 = input("Введите,пожалуйста, кол-во  дней: ")
#day = int(user_input1)
#print('Вы ввели', day)

if (month == 0)or (month < 0) or (month > 12):
    print('номер месяца некорректен')
elif (month == 4) or (month == 6) or (month == 9) or (month == 11) :
    print(month, ':',  days[1])
elif month == 2:
    print(month, ':', days[0])
else:
    print(month, ':', days[2])

# Зачет!++++
