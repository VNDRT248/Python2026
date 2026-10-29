text = input('Введите текст: ')
words = text.split()
count = 0
for w in words:
    clean = w.strip('.,!?;:').lower()
    if clean == '':
        continue
    if clean.startswith('к'):
        print(clean)
        count = count + 1
if count == 0:
    print('Нет совпадений')
print('Количество:', count)