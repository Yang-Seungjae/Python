# 정수 2개 입력받아 최대 공약수 출력
print ( f'정수 a를 입력하세요 :')

a = input()

print ( f'정수 b를 입력하세요 :')

b = input()


for i in a :
     if a % i == 0:
         print(i)
