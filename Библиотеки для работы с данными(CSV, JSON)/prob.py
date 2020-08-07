d = {
    1: 'a',
    2: 'b',
    3: 'c',
   }
copy = d.copy()
for key in copy:
    delete = d.pop(key)
    d[key] = delete
    print(delete)
print(d.pop(1))