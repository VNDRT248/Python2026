import math

while True:
    rad = float(input('Введите радиус окружности: '))
    if rad > 0:
        break
    else:
        print('Ошибка! Радиус должен быть положительным')

dlin = 2 * math.pi * rad
plosch = math.pi * rad ** 2

print(f'Длина окружности: {dlin:.2f}')
print(f'Площадь круга: {plosch:.2f}')