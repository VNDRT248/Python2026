s = input('Введите целые числа: ')
parts = s.split()
a = []
for p in parts:
    a.append(int(p))
b = []
for x in a:
    if x < 0:
        b.append(-x)
    else:
        b.append(x)
print('Исходный:', a)
print('Новый:', b)