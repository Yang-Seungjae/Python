data = [10,20,30,40] #리스트
print(data)
print(*data) #print(10,20,30,40) 리스트에 있는 데이터를 각각 뽑아서 출력 ->unpacking

def getTotal(a,b,c,d):
    return a+b+c+d


print(f'총합: {getTotal(1,2,3,4)}')
print(f'총합: {getTotal(10,20,5,6)}')
print(f'총합: {getTotal(*data)}') # 정수값의 요소로 날라가게 하고싶음




# def getSum(*nums):
#     s=0
#     for n in nums:
#         s += n
#     return s

def getSum(*nums):  # 인자가 몇개인지 모를때
    # print(nums,type(nums))
    s=0
    for n in nums:
        s+=n
    return s
print(getSum(10,20,30,40))
print(getSum(10,20,30,40,50,60))
print(getSum(10,20))

#팩킹을 해서 리스트로 보고싶음

