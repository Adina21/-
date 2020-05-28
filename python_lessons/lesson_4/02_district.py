# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join


from district.central_street.house1.room1 import folks as str1

from district.central_street.house1.room2  import folks as str2

from district.central_street.house2.room1 import folks as str3

from district.central_street.house2.room2 import folks as str4

from district.soviet_street.house1.room1 import folks as str5

from district.soviet_street.house1.room2 import folks as str6

from district.soviet_street.house2.room1 import folks as str7

from district.soviet_street.house2.room2 import folks as str8

string = str1 + str2 + str3 + str4 + str5 + str6 + str7 + str8
print('На районе живут:', ', '.join(string))
#зачет!