from functions import average,normalize_text,sum_digits,select_numbers,is_palindrome
assert sum_digits(0)==0
assert sum_digits(507)==12
assert sum_digits(-507)==12
assert average([]) is None
assert average([2,4,6])==4
assert normalize_text("  ПРИВЕТ   Мир  ")=="привет мир"
assert normalize_text("   ")==""
assert select_numbers([-5,0,2,5],2)==[2,5]
assert select_numbers([],2)==[]
assert select_numbers([1,2,3],2)==[2,3]
assert select_numbers([2,2,3],2)==[2,2,3]
a=[1,2,3]
b=a.copy()
select_numbers(a,2)
assert a==b
assert is_palindrome("А роза упала на лапу Азора")==True
assert is_palindrome("   ")==False
assert is_palindrome("Python")==False
print("Базовые проверки пройдены")