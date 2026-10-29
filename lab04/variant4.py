while True:
    n = int(input('Сколько будет чисел? '))
    if n >= 0:
        break
    else:
        print('Ошибка!')
kol = 0
summa = 0
i = 0
while i < n:
    x = int(input('Введите число: '))
    if x % 2 != 0:
        kol = kol + 1
        summa = summa + x
    i = i + 1
print('Количество нечетных:', kol)
print('Сумма нечетных:', summa)