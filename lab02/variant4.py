while True:
    total = int(input('Введите общее количество деталей: '))
    if total >= 0:
        break
    else:
        print('Ошибка! Количество деталей не может быть отрицательным')

while True:
    capacity = int(input('Введите вместимость одного контейнера: '))
    if capacity > 0:
        break
    else:
        print('Ошибка! Вместимость должна быть положительной')

full = total // capacity
ostatok = total % capacity
containers = (total + capacity - 1) // capacity

print(f'Полных контейнеров: {full}')
print(f'Остаток деталей: {ostatok}')
print(f'Всего контейнеров нужно: {containers}')