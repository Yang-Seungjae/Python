'''
    list 내장함수
    append : 데이터 추가 (맨마지막)
    insert : 데이터 추가 (특정위치)

    pop    :데이터 삭제 (맨마지막) 인덱스 쓸 수 있음
    remove :데이터 삭제 (특정위치)

    index  : 특정값 위치 검색
    count  : 특정값의 빈도수

    reverse : 역정렬
    sort    : 정렬
    clear  : 리스트 요소 전부 삭제

    stack LIFO
    queue FIFO
'''

data = []
print(data, id(data))
data.append(10)
data.append(20)
data.append(30)
print(data, id(data))
delData= data.pop()
print('삭제된 값: ',delData) # 스택처럼 만든 방식

data = list()
data.insert(0, 10)
data.insert(0, 20)
data.insert(0, 30)
print(data, id(data))
delData=data.pop()
print('삭제된 값: ',delData)

# 큐처럼 쓸 때
data=[]
data.append(10)
data.append(20)
data.append(30)
print(data,id(data))
delData = data.pop(0)
print('삭제된 값: ',delData)

data=[10,20,30,40,30]
idx = data.index(30) # 여러번 있으면 맨 처음? 앞쪽에 있는애 가 나옴
cnt = data.count(30)
print('위치: ',idx)
print('개수: ',cnt)
print('before: ',data)
data.remove(30)
print('after: ',data)

for i in range(len(data)):
    print(data[i], end=' ')
print()

# ite = iter(data)
# print(next(ite))
# print(next(ite))
# print(next(ite))
# print(next(ite))
# print(next(ite))

data.reverse()
for d in iter(data):
    print(d, end=' ')
print()

# print(data[-1])
# print(data[-2])
data.reverse()

# data2=reversed(data)
# print('data: ',data)
# print('data2: ',next(data2))

for d in reversed(data):
    print(d, end=' ')
print()

# data.sort()
# print(data)

print(sorted(data)) #reversed = False (default, 오름차순) =True(내림차순)
print(data)

data = [10,20,30]
# print(data.pop())
# print(data.pop()) 이러면 에러남

# for i in range(len(data)):
#     # data.pop(0)
# print(data)
# 위 방법은 무식해 보임

# data.clear() #다 지우는 명령어
# del data[:]
# print(data)


ite = iter(data)

for d in iter(data):
    print(d,end=' ')
print()

# for index, d in enumerate(data, start=100): #스타트 값을 넣어서 제어가능
for index, d in enumerate(data):
    print(f'[{index}] : {d}')

for i in range(1,len(data)+1):
    print(data[-i], end=' ')
print()



data=[10,40,20,70,50,60,30,50]
# maximum = data[0]
# minimum = data[0]
# for d in data:
#     if minimum>d:
#         minimum =d
#     if maximum<d:
#         maximum=d
# 위 방법은 지저분하자나

sortData=sorted(data)
maximum = sortData[-1]
minimum = sortData[0]

print(f'가장큰 수 : {maximum}, 가장 작은 수 : {minimum}')
print(f'가장큰 수 : {max(data)}, 가장 작은 수 : {min(data)}')
print(f'총합: {sum(data)}')

# 1~100 사이의 정수 10개를 원소로 가지는 리스트 data 선언


#방법 2
#data = list()
# for i in range(10):
#     data.append(i+1)

#방법3
data = [i+1 for i in range(10)]
print(data)

# 홀수만 집어넣기
# data = [i+1 for i in range(10) if (i+1)%2]
# print(data)

data = [2*i+1 for i in range(5)]
print(data)


# 구구단 데이터 생성
dan = 4
guguData=[dan*i for i in range(1,10)]
print(guguData)

#2~9단 값
guguData=[dan*i for dan in range(2,10) for i in range(1,10)]
print(guguData)


#글자수세서 데이터 추출
strData=['hello','good','bye','welcome','apple','sorry']
fiveStrData=[s for s in strData if len(s)==5]
print(fiveStrData)

copyStrData=strData[:]
copyStrData2=strData.copy()


print('strData: ', strData,id(strData))
print('copyStrData: ',copyStrData, id(copyStrData))
print('copyStrData: ',copyStrData2, id(copyStrData2))


# 밑에 코드로 하면 에러남 (튜플은 추가 할 수 없어서)
# tupleData = tuple()
# tupleData.__add__(10)
# print(tupleData)


