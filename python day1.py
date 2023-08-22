print('첫번째 정수를 입력 : ', end='')
#end 는 출력된 문자열의 끝을 어떻게 처리할지를 지정하는 역할을 합니다.
num01 = int(input())
print(type(num01))
'''
이것은 여러 줄 주석입니다
'''

#이것은 한줄 주석입니다

"""
이것도 여러줄 주석입니다
"""
print('두번째 정수를 입력 : ', end='')
num02 = int(input())

print(num01, num02, sep=":")
#sep 는 두개의 입력값 사이를 어떤것으로 구분할지 지정할 수 있습니다.

print(num01, '+', num02, '=', num01 + num02)

#,를 이용해서 사칙연산을 할 수 있지만 불편한 방법입니다

print('%d - %d = %d' %(num01,num02,num01-num02))
print('%d * %d = %d' %(num01,num02,num01*num02))


#formating을 이용할경우 %기호를 사용합니다. % () 안에 인자의 개수만큼 넣으면 됩니다.


print('%d / %d = %d' %(num01,num02,num01/num02))
print(num01/num02)

#파이썬은 변수의 자료형을 자동으로 변환하기 때문에 위의 두개의 결과값이 다르게 나옵니다. 이러한 불편한점을 해결하려고 다른 포맷팅 방식이 존재


print('{0} / {1} = {2}'.format(num01, num02, num01 / num02 ))


print(f'{num01} / {num02} = {num01 / num02}') # 매번 .format을 적기가 귀찮아서 앞에 f를 붙여주면 format하겠다는 의미가 된다

#몫만 구하고 싶으면 // 이렇게 적어야함 나머지값을 구하고싶을때 % 로 사용
print(f'{num01} / {num02} = {num01 // num02}')

#제곱승에 관한 내용 2의 3승을 표현할때 2 ** 3 이렇게 표현가능

#파이썬에서 *는 다양한 기능을 하는데

print(2 * 3)  # 여기에서는 곱하기의 사칙연산 기호지만

print('2' * 3) #이런식으로 문자열을 * 해버리면 반복을 의미한다


# 여러개의 input을 한번에 받고싶을때

num01, num02 = map(int, input('두개의 정수를 입력 : ').split())
print(num01, num02)
print(type(num01), type(num02))

#map(int , ['12', '5']) 이것의 의미는 문자열로가진 12, 5를 인트형으로 인식하고싶은것

#연산자에서 주의해야 할것들

'''
논리값(True) 이런형태로 앞에 t를 대문자로 적으면 참, 거짓을 표현할 수 있다.
print( 10 > 3 ) 
print( 10 == 3)
print( 10 != 3)
print("Hello" == "Hello")

print(1 == 1.0) 이건 어떻게 될까 ? ==> 값비교를 하기때문에 True로 나오는데 
실제 1 은 정수형 1.0은 float형으로 다르다 
이럴때 is를 사용해서 비교한다
print(1 is 1.0) ==> false 로 출력 자바스크립트의 ===와 같은기능

'''

print(id(1))
print(id(1.0))

# id는 주소까지 비교함

print('Hello')
print("Hello")
print("""Hello
여러줄도 가능하다 """)

data = [10, 20, 30, 40] #List 타입은 이렇게 표현
print(type(data), data)
data = list()
print(type(data), data)

data = (10, 20, 30, 40) #10, 20, 30, 40 과 같다 괄호를 안해도 tuple로 인식한다
print(type(data), data)
data = tuple()
print(type(data), data)

data = range(10)
print(type(data), data)
#출력을 위해서
data = list(data)
print(data)

data = range(5, 15)
print(list(data))

data = list(range(1,10,2)) #1에서 10까지 +2씩 출력하기
print(data)

data = list(range(20, 4, -3))
print(data)

# in과 [ : ]  슬라이스
print(16 in data, 17 in data)  # ==> false, true 순으로 출력됨

print('e' in 'Hello')

data = list(range(1, 10))
print(data)

print(data[0:5])

# 기존의 데이터를 건들지 않고 슬라이스를 활용하려면

data2 = data[0:5]
print(data)
print(data2)
print(data[5:8])

print(data[:3]) # 앞에가 없으면 0부터로 인식
print(data[3:]) # 뒤에가 없으면 length 까지로 인식
print(data[:])


print(data)
data2 = data #shallow copy - 새로운 객체를 생성하지만 원래 객체의 요소들은 원본 객체와 같은 객체를 참조
data2 = data[:] #deep copy - 새로운 객체를 생성하면서 원래 객체의 모든 요소를 재귀적으로 복사 / 원본과 완전히 독립적 서로 영향 x
print(data2)
data2[0] = 100
print(data)


print(data[5:len(data)])
print(data[5:-1]) # print(data[5:len(data) - 1]) 과 같은 의미

print(data[2:8:2])
print(data[2::2])
print(data[8:2:-2])
print(data[::-1]) # 거꾸로 끝에서부터 시작지점까지 출력이라는 뜻


data[2:5] = [100,200,300] #꼭 3개를 넣어야하는건 아님 하나만 넣을 수도있음 그럼 배열의 길이가 바뀜

print('data : ',data)

data[2:6:2] = [10,20]

#del 함수를 이용해서 데이터 삭제도 가능

del data[2:5]








