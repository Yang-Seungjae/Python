data=set()
print(f'{data} 원소의 개수: {len(data)}')
for i in range(10):
    data.add(i+1)

data.add(5)
data.add('5')
print(f'{data} 원소의 개수 : {len(data)}')
data.remove('5')
data.remove(5)

print(f'pop("5")후{data} 원소의 개수: {len(data)}')
# data.remove('5')  # in 키워드를 통해서 존재하는지 먼저 확인 후 지워야됨. 없는 데이터를 지우면 에러남
data.discard('5')
print(f'discard("5")후{data} 원소의 개수: {len(data)}') # 없을때 써도 에러안남

# copy=data # 얕은복사
copy=data.copy() #깊은복사
print(f'data:{data}')
print(f'copy:{copy}')
copy.add(5)
print(f'data:{data}')
print(f'copy:{copy}')
