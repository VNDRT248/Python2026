# 4	вар | Художественная мастерская	| Альбомы | Наборы кистей
nazvan_zak = input('Введите название заказа:')
name_zak = input('Введите имя заказчика:')
pos1_naz = input('Введите название первой позиции:')
pos2_naz = input('Введите название второй позиции:')
while True:
    pos1_kolvo = int(input('Введите количество первой позиции:'))
    if pos1_kolvo >= 0:
        break
    else:
        print('Ошибка! Количества — целое неотрицательное число.')
while True:
    pos2_kolvo = int(input('Введите количество второй позиции:'))
    if pos2_kolvo >= 0:
        break
    else:
        print('Ошибка! Количества — целое неотрицательное число.')

while True:
    pos1_money = float(input('Первая позиция. Введите цену единицы в рублях:'))
    if pos1_money >= 0:
        break
    else:
        print('Ошибка! Цена — неотрицательное дробное число.')
while True:
    pos2_money = float(input('Вторая позиция. Введите цену единицы в рублях:'))
    if pos2_money >= 0:
        break
    else:
        print('Ошибка! Цена — неотрицательное дробное число.')
while True:
    dost = float(input('Введите стоимость доставки:'))
    if dost >= 0:
        break
    else:
        print('Ошибка! Стоимость доставки не может быть отрицательной.')

stoim1 = pos1_kolvo * pos1_money
stoim2 = pos2_kolvo * pos2_money
stoim_1i2 = stoim1 + stoim2
dost_stoim = stoim_1i2 + dost

while True:
    vnes_summ = float(input('Введите внесённую сумму:'))
    if vnes_summ >= dost_stoim:
        break
    else:
        print('Ошибка! Внесённая сумма не меньше стоимости обеих позиций с доставкой.')

obsh_kolvo = pos1_kolvo + pos2_kolvo
cdacha = vnes_summ - dost_stoim

print('-' * 70)
print(f'Заказ: {nazvan_zak}')
print(f'Заказчик: {name_zak}')
print('-' * 70)
print(f'Название:{pos1_naz} | Количество:{pos1_kolvo} | Цена:{pos1_money:.2f} | Стоимость:{stoim1:.2f}')
print(f'Название:{pos2_naz} | Количество:{pos2_kolvo} | Цена:{pos2_money:.2f} | Стоимость:{stoim2:.2f}')
print('-' * 70)
print(f"Общее количество единиц: {obsh_kolvo}")
print(f"Стоимость товаров без доставки: {stoim_1i2:.2f}")
print(f"Стоимость доставки: {dost:.2f}")
print(f"Общая сумма с доставкой: {dost_stoim:.2f}")
print(f"Сдача: {cdacha:.2f}")
print("-" * 70)
