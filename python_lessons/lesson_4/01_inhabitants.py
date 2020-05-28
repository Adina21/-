# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

from room_1 import folks as f1
from room_2 import folks as f2

print('В комнате room_1 живут:', ', '.join(f1))
print('В комнате room_2 живет:', ''.join(f2))

#зачет!