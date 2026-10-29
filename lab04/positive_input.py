popitki = 0
while True:
    x = int(input('Введите положительное число: '))
    if x > 0:
        break
    else:
        print('Ошибка!')
        popitki = popitki + 1
kvadrat = x * x
print('Квадрат числа:', kvadrat)
print('Отклонено попыток:', popitki)