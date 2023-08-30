import random

r = int(random.random() * 10 )

print(r)

#if 문
if r % 2 == 0:
    print(f'{r} : 짝수')
else:
    print(f'{r} : 홀수')

if num < 0 :
    print('짝/홀 판단은 양수만 가능')
elif num % 2 == 0:
    print(num, ': 짝수')
else :
    print(num, ': 홀수')


#while 문
num = 1
while num <= 10:
    print(num, end=' ')
    num += 1

#for 문

for i in range(1,11):
    print(i, end=' ')

'''
for i in range(10)
    print(i+1, end='')
이것과 위에 것이 같다
'''
'''
*
**
***
****
*****
'''
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()

for i in range(5):
    print('*' * (i+1))

'''
*
* *
*  *
*   *
*  *
* *
*

'''


for i in range(9):
    if i < 5:
        print('*' * (i+1))
    else:
        print('*' * (9-i))

#파이썬에서 조건연산자
'''
for i in range(9):
    참문장 if 조건식 else 거짓문장
    print('*' * cnt)
'''
for i in range(9):
    cnt = (i+1) if i < 5 else (9-i)
    print('*' * cnt)