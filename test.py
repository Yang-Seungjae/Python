# quit가 나올때까지 정수를 입력받아 각 정수의 약수를 출력
# 10
# 6
# 36
# 87
# 23
# 40
# quit
# 10의 약수 : [1 2 5 10]
# 6의 약수 : [1 2 3 6]
# 36의 약수 : []

data = []
str = ""
while str != 'quit':
    print('정수를 입력하세요 : ')
    str = input()
    data.append(str)