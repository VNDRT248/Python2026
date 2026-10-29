s = input('Введите целые числа: ')
parts = s.split()
a = []
for p in parts:
    a.append(int(p))
b = []
for x in a:
    if x % 2 != 0:
        b.append(x)
kol = len(b)
summa = sum(b)
c = sorted(b)
print('Выборка:', b)
print('Количество:', kol)
print('Сумма:', summa)
print('Отсортированная копия:', c)