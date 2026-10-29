text = input('Введите текст: ')
clean = text.lower().replace(' ', '')
if clean == '':
    print('Нет текста')
else:
    if clean == clean[::-1]:
        res1 = 'Палиндром'
    else:
        res1 = 'Не палиндром'
    is_pal = True
    left = 0
    right = len(clean) - 1
    while left < right:
        if clean[left] != clean[right]:
            is_pal = False
            break
        left = left + 1
        right = right - 1
    if is_pal == True:
        res2 = 'Палиндром'
    else:
        res2 = 'Не палиндром'
    print('Срез:', res1)
    print('Цикл:', res2)
