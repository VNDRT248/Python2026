while True:
    price = int(input('Введите цену одной тетради в рублях: '))
    if price >= 0:
        break
    else:
        print('Ошибка! Цена не может быть отрицательной')

while True:
    count = int(input('Введите количество тетрадей: '))
    if count >= 0:
        break
    else:
        print('Ошибка! Количество не может быть отрицательным')

cost = price * count

while True:
    paid = int(input('Введите переданную сумму: '))
    if paid >= cost:
        break
    else:
        print('Ошибка! Переданная сумма меньше стоимости')

sdacha = paid - cost

print(f'Стоимость: {cost}')
print(f'Сдача: {sdacha}')