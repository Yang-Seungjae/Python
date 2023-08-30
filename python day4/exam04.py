'''
open(파일명, 모드) # 'r' "w"모드
read(), write()
close()

with open() as 파일객체:
    read()/write() 들여쓰기 해야함 위에 콜론때문에

'''

# file = open('test.txt',"w") # 없으면 파일생성됨
# file.write('hello')
# file.close() # 다썼으면 닫아주기


#읽기
# file = open('test.txt',"r") # 없는파일이면 예외 오류남
# data = file.read()
# file.close()

with open('test.txt','r') as file:
    data=file.read()
print(f'읽어온 데이터: {data}')