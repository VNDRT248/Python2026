def sum_digits(number):
    a=abs(number)
    s=0
    while a>0:
        s=s+a%10
        a=a//10
    return s
def average(numbers):
    if len(numbers)==0:
        return None
    s=0
    for x in numbers:
        s=s+x
    return s/len(numbers)
def normalize_text(text):
    return ' '.join(text.lower().split())
def select_numbers(numbers,threshold):
    b=[]
    for x in numbers:
        if x>=threshold:
            b.append(x)
    return b
def is_palindrome(text):
    t=text.lower().replace(' ','')
    if t=='':
        return False
    if t==t[::-1]:
        return True
    else:
        return False