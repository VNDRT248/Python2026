a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
if a < b:
    while a <= b:
        print(a)
        a = a + 1
elif a > b:
    while a >= b:
        print(a)
        a = a - 1
else:
    print(a)