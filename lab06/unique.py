s = input('Введите целые числа: ')
parts = s.split()
a = []
for p in parts:
    a.append(int(p))
b = []
for x in a:
    if x not in b:
        b.append(x)
print('Без повторов:', b)