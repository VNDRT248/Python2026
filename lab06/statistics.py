s = input('Введите целые числа: ')
parts = s.split()
if len(parts) == 0:
    print('Нет данных')
else:
    a = []
    for p in parts:
        a.append(int(p))
    kol = len(a)
    summa = sum(a)
    minn = min(a)
    maxx = max(a)
    sr = summa / kol
    print('Количество:', kol)
    print('Сумма:', summa)
    print('Минимум:', minn)
    print('Максимум:', maxx)
    print(f'Среднее: {sr:.2f}')