from functions import sum_digits,average,normalize_text,select_numbers
def main():
    a=int(input('Введите целое число: '))
    print('Сумма цифр:',sum_digits(a))
    s=input('Введите числа через пробел: ')
    parts=s.split()
    nums=[]
    for p in parts:
        nums.append(int(p))
    avg=average(nums)
    if avg==None:
        print('Среднее: Нет данных')
    else:
        print(f'Среднее: {avg:.2f}')
    t=input('Введите текст: ')
    print('Текст:',normalize_text(t))
    p=int(input('Введите порог: '))
    res=select_numbers(nums,p)
    print('Выборка:',res)
if __name__=='__main__':
    main()