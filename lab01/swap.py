first_room = input('Введите название первой аудитории: ')
second_room = input('Введите название второй аудитории: ')

print(f'Исходные значения: {first_room}, {second_room}')

temp = first_room
first_room = second_room
second_room = temp

print(f'Результат: {first_room}, {second_room}')