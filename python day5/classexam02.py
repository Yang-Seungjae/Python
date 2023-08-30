class Person :

    '''
    def __del__(): 삭제할때마다 어떤 작업을 실행시키고 싶을때 쓰는 코드

    '''
    def __init__(self,name, age, addr ):
        self.name = name
        self.age = age
        self.__addr = addr

    def getAddr(self):
        return self.__addr

    def setAddr(self, addr):
        self.__addr = addr

    def info(self):
        print(f'name : {self.name}, age : {self.age}, addr : {self.__addr}')


p = Person('홍길동', 25, '서울')
p.info()
print(p.name)
print(p.age)
#print(p.__addr) 이런식으로 __ 붙이면 외부에서는 접근할수없는 비공개 형태로 바뀐다
print(p.getAddr())
#외부에서 p.addr 를 출력하면 서울이 나오게 만들고 싶다면 get 메소드의 이름을 addr로 만들고 @property 를 설정해주면된다
#변수처럼 사용하면 get 메소드가 호출되게 만드는것 외부에서는 변수처럼 보이지만 실제론 함수

    @property
    def addr(self):
        return self.__addr

