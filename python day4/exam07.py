'''

def 함수 (인자,인자):
    문장
    문장
    return
'''

def add(a, b):
    return a+b

def sub(a,b):
    return a-b

def mul (a,b):
    return a * b

def div (a,b):
    return a/b

print(f'덧셈: {add(12,7)}')
print(f'뺄셈: {sub(12,7)} ')
print(f'곱셈: {mul(12,7)} ')
print(f'나눗셈: {div(12,7)} ')

def calculate(a, b):
    return add(a,b), sub(a,b), mul(a,b), div(a,b)
print(calculate(12,7))
#list = calculate(12,7) 이렇게도 받을 수 있지만
a,b,c,d = calculate(12,7) # 날아간 데이터들을 언패킹으로 이렇게 가능

