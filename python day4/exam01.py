data=set([1,2,3,4])
print(type(data),data)
data2={1,2,5,6}
print(type(data2),data2)

print(f'합집합(data,data2): {data.union(data2)}')  #union 합집합으로 만들어줌. 데이터들은 원본 유지
print(f'합집합(data,data2): {data | (data2)}')  #union 합집합으로 만들어줌. 데이터들은 원본 유지
print(f'교집합(data,data2):{data.intersection(data2)}')
print(f'교집합(data,data2):{data & data2}')
print(f'차집합(data,data2): {data.difference(data2)}') #data-(data,data2 교집합)
print(f'차집합(data,data2): {data - data2}') #data-(data,data2 교집합)
print(f'대칭차집합(data,data2): {data.symmetric_difference(data2)}')# 합집합-차집합
print(f'대칭차집합(data,data2): {data^data2}')# 합집합-차집합

print(data,data2)