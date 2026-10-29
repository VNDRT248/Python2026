s = input('Введите целые числа: ')
parts = s.split()
a = []
for p in parts:
    a.append(int(p))
if len(a) == 0:
    print('Нет данных')
else:
    maxx = max(a)
    b = []
    for i, x in enumerate(a):
        if x == maxx:
            b.append(i)
    print(b)