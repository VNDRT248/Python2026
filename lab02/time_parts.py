while True:
    total_seconds = int(input('Введите количество секунд: '))
    if total_seconds >= 0:
        break
    else:
        print('Ошибка! Число секунд не может быть отрицательным')

total_hours = total_seconds // 3600
ostat = total_seconds % 3600
total_minutes = ostat // 60
total_seconds = ostat % 60

print(f'{total_hours} ч {total_minutes} мин {total_seconds} с')