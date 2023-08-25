'''
10
6
36
87
23

quit
10의 약수[1,2,5,10]
6의 약수 [1,2,3,6]
36의 약수[1,2,3,4,6,9,12,18,36]
...
40의 약수[1,2,4,5,8,10,20,40]

'''


print('정수를 입력하시오. quit입력시 종료됩니다')

inputs=list()
while True:
    data=input()
    # if data == 'quit':
    #  quit, Quit,QUIT 이라고 입력할 수도 있는데 모든 경우의 수를 쓸 순 없잖아
    if data.lower() == 'quit':
        break
    inputs.append(int(data))

for num in inputs:
    div = [i+1 for i in range(num) if num % (i+1)==0]
    print(f'{num}약수 :

--------------------------------------------------------------------------------------------------------------
str="Hello World"
print(str, str.upper(),str.lower())
print(str)
#.upper, .lower를 쓰면 출력만 대소문자로 해주고 원본데이터 문자열은 바뀌지 않음

strList = str.split()
print(strList)

# str2="Hello, World"
# print(str2, str2.upper(),str2.lower())
# print(str2)
#
# strList2 = str2.split(',') # ',' 기준으로 잘려서 world 앞에 스페이스까지 데이터로 들어감
# print(strList2)

str = "Hello, World"
print(str, str.upper(), str.lower())
strList = str.split(',')
print(strList)
str2 = '/'.join(strList)
print(str2)
print(f'[{strList[1].lstrip()}]')

str = ' !   Hello World    '
print(f'lstrip(): [{str.lstrip(" !")}]')
print(f'rstrip(): [{str.rstrip()}]')
print(f'strip(): [{str.strip("! ")}]')


str='hello'
print(f'str : [{str}]')
print(f'str : [{str.center(11)}]')# 공백수가 짝수면 좌우 균등하게 공백생성, 홀수로 남으면 오른쪽에 한칸 더 배분
print(f'str : [{str.center(10)}]')
print(f'str : [{str.ljust(10)}]')
print(f'str : [{str.rjust(10)}]')
print(f'str : [{str.zfill(10)}]') #앞에 0으로 공백채움


str = 'Hello World!!'
# 문자열이 몇번째에 위치하고 있는지 알고싶음
print(f'"o"의 위치: {str.index("o")}') # 해당 문자열이 없는 경우 예외발생
print(f'"o"의 위치: {str.rindex("o")}') # 오른쪽에서부터 왼쪽으로 검색
print(f'"o"의 위치: {str.index("o",6)}') #뒤에 숫자 입력하면 해당 수 인덱스부터 검색
print(f'"o"의 위치: {str.find("o")}') # 해당 문자열이 없는경우 -1 반환
print(f'"o"의 위치: {str.rfind("o")}') # 오른쪽에서부터 왼쪽으로 검색
print(f'"l"의 개수: {str.count("l")}') # 같은 문자열 개수
print(f'"l" => "rr" 변환: {str.replace("l","rr")}') # 해당 문자열 다른 문자열로 치환

--------------------------------------------------------------------------------------------------------------------

data = {'hong':1111, 'kang':2222,'han':3333, 'park':4444, 'kang':5555, 100:'123'}
# 중복된 key가 들어가면 에러가 나진 않지만 원래 키의 데이터가 마지막 key의 데이터로 업데이트 돼서 하나만 찍힘
# 키에 문자열뿐만 아니라 정수 형태도 들어갈 수 있음
print(data, type(data))

stuInfo={'name':'hong', 'age':28, 'scores':[100,100,70]} # 리스트 딕셔너리 튜플의 형태가 들어갈 수 도 있음
print(stuInfo)

data={}
data = dict()
data =dict(name='kang', age=28, addr='seoul')

# key값에 ' ' 안씀. 밸류에 ' ' 붙이면 문자열, 안붙이면 정수형  -> key=value형태로 입력할 땐 key에 문자열 형태만 입력가능함 1 = 100 이거 안됨
data = dict([('name','hong'),('age',28),('addr','seoul'),(100,'max')])
print(data,type(data))   # 비어있어도 딕셔너리 로 찍힘

# key:value를 초기화 할 수 있는 애들?

#ZIP객체 를 딕셔너리형에 넣어서 딕셔너리 형태가 되는 것
data = dict(zip(['name','age','addr'],['hong',28,'soeul']))
# data = dict(zip(['name','age','addr'],['hong',28,'soeul'],['kang',30,'soeul']))
# 위처럼 두개 이상은 에러남...
print('zip객체 사용',data,type(data))

----------------------------------------------------------------------------------------------------------------

'''
     setdefault   : 새 데이터 삽입
    update       : key 없으면 데이터 삽입, key 없으면 데이터 수정
    pop          : 데이터 삭제
'''



members = {'홍길동':'010-1111-2222','박길동':'010-3333-4444'}
print(members)
members.setdefault('윤길동','010-5555-6666')
members.setdefault('이길동') # value값이 없으면 none으로 들어감
print(members)


# members.setdefault('이길동','010-8888-7777')
# setdefault는 기존 key값을 수정할 수는 없음. -> 이런식으로 밸류값 삽입 불가능
#새데이터 삽입o, 데이터 수정 x
print(members)

# key값이 있을경우 기존 value 데이터값 수정-> update사용 , key값이 없으면 새로운 데이터 추가
# = 이퀄형태라 정수형 key는 불가능
members.update(이길동='010-8888-7777')
members.update(한길동='010-9999-7777')
print(members)


# members.update(202308501='010-2345-6789') -> '='equal형태는 키값에 정수형 사용 불가 =>에러남
members.update({202308501:'010-2345-6789'})
members.update([[2023082502,'010-1234-5678'],[2023082503,'010-9876-5432']])
members.update(zip(['park','이길동'],['8282',None]))  #-> park-8282 키-밸류 추가, 이길동은 none으로 업데이트
print(members)

#딕셔너리형태에 딕셔너리 value값이 들어갈 수 있음
#이런경우는 pandas많이 사용


value = members.pop('이길동')
print(f'pop("이길동"):{value}')
members.pop('구길동',"없음") #pop에 key가 없는 값이면 리턴할 값이 필요
print(members)

members.popitem() # 맨 마지막 키-밸류값 삭제
print(members)

# clear 함수는 전체 데이터 삭제

# get 데이터 조회
value = members.get('홍길동')
print(f'홍길동: {value}')
print(f'이길동: {members.get("이길동")}')
print(f'이길동: {members.get("이길동","존재하지않음")}') # 값이 none일 경우 다른 대체 텍스트가 나오게 할 경dn

-----------------------------------------------------------------------------------------------------------

members = {'홍길동':'1111-2222','박길동':'3333-4444','윤길동':'5555-6666'}
#홍길동 존재여부
print(f'홍길동 존재여부 : {"홍길동" in members}')
print(f'고길동 존재여부 : {"고길동" in members}')

# key값들만 출력
print(members.keys())
# value값들만 출력
print(members.values())
# key-value 모두 풀력
print(members.items())

for data in members:
    # print(data, end='')
    print(f'{data} : {members.get(data)}')
print()

------------------------------------------------------------------------------------
members = {'aaa' : '1111', 'bbb' : '2222', 'ccc': '3333', 'ddd':'4444'}

print('패스워드 변경서비스입니다')
id = input('아이디를 입력하세요 :')

if id in members: #not in으로 할수도있따
    pass
else :
    print(f'입력하신 아이디 [{id}] 는 존재하지 않습니다')
    print(f'패스워드 변경서비스를 종료합니다')
    exit(0)

password = input('현재 패스워드를 입력하세요 :')
if members.get(id) != password:
    print(f'패스워드가 일치하지 않습니다 ')
    print(f'서비스를 종료합니다')
    exit(0)

newPassword = input('변경할 패스워드를 입력하세요: ')
# members.update(id=newPassword') # id자체가 변수가 아닌 상수로 인식되어버림-> 이 방법엔 문제가 존재하기 때문에 리스트 형식을 쓰던지 딕셔너리 형태를 사용해야 함
members.update([[id,newPassword]]) # 리스트 형태
# members.update({id:newPassword}') # 딕셔너리 형태로
members[id] = newPassword

print('<전체 회원 목록>')
print('아이디\t패스워드')
for id,pw in members.items():
    print(f'{id:<6}\t{pw}')


members = {keys:value}

keys = ['name', 'age', 'addr']

members = {key:value for key, value in dict.fromkeys(keys).item()}
print(members)

members = {'홍길동':'32거2345','고길동':'26소2756','윤길동':'89나2134'}

print(members.get('홍길동')) #

#차량번호의 소유주 검색

mem = {value:key for key, value in members.items()}
print(mem.get('26소2756'))

data = [key for key, value in members.items()
        if value == '26소2756']
print(data[0])


#
# for key, value in members.items():
#     if value == '26소2756':
#         print(key)
#         break