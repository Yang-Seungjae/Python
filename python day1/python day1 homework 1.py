# import random
#
# r = int(random.randint(20, 50))
#
# print(r)
# for i in range(r):
#     if '33' in str(i):
#         print('짝짝')
#     elif '36' in str(i):
#         print('짝짝')
#     elif '39' in str(i):
#         print('짝짝')
#     elif i%10 == 0:
#         print('뽀' * (i//10),'숑')
#     elif '3' in str(i):
#         print('짝')
#     elif '6' in str(i):
#         print('짝')
#     elif '9' in str(i):
#         print('짝')
#     else :
#         print(i)
#

import random

r = random.randint(20, 50)

print(r)
for i in range(1, r + 1):
    output = ''
    if i % 10 == 0:
        output = '뽀' * (i // 10) + '숑'
    elif '3' in str(i) or '6' in str(i) or '9' in str(i):
        output = '짝' * (str(i).count('3') + str(i).count('6') + str(i).count('9'))
    else:
        output = i
    print(output)


