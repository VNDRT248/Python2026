while True:
    n = int(input('Сколько будет чисел? '))
    if n >= 1:
        break
    else:
        print('Ошибка!')
x = int(input('Введите число: '))
summa = x
polozh = 0
maxx = x
if x > 0:
    polozh = 1
i = 1
while i < n:
    x = int(input('Введите число: '))
    summa = summa + x
    if x > 0:
        polozh = polozh + 1
    if x > maxx:
        maxx = x
    i = i + 1
print('Сумма:', summa)
print('Количество положительных:', polozh)
print('Максимум:', maxx)