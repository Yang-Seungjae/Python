class Dog:
    pass
dog = Dog()
print(type(dog))

class Car:
    def drive(self): # self가 붙으면 클래스 내부의 내장함수라고 생각하면된다 일반 함수와 클래스 내부의 함수를 구분하기 위해 적어줌
        pass

        c = Car()
        c.drive()
        print(f'type(Car) 판단:  {isinstance(c, Car)}')
        print(f'type(Car) 판단:  {isinstance(10, Car)}')
        print(f'type(Car) 판단:  {isinstance([10,20,30], Car)}')

        l = [10, 20, 30]
        print(l[0], l.__getitem__(0)) # , 좌우에 있는게 같다 내장함수 호출에 __ __를 쓰는데 보다 쉽게 쓰기위한 방법이많다

        #def__init__(): 생성자 역할을 한다


class TV:
    def __init__(self):   #self 자리에
        # print('초기화 진행')
        self.power = False
        self.channel=10

    def info(self):
        print(f'채널정보: {self.channel}')
        if 'volume' in self.__dict__:
              print(f'음량: {self.volume}')

tv=TV()
print(tv.power)  # self키워드를 쓰면 퍼블릭한 클래스에서 멤버변수로 사용 가능
# tv.info()
tv.volume=20
print(tv.volume) # 멤버변수를 직접 넣을 수 있음
tv.info()


class Car :

    addr = '서울'  #static 변수 역할

    __slots__ = ['name', 'price', 'company'] # 슬롯 . 이 클래스가 가질 수 있는 멤버변수명을 미리 지정해 줄 수 있다.
    def __init__(self, **args):
        if 'name' in args:
            # self.add(value) #이런식으로 넣을 수 없음 의미가없다.
            self.name = args['name']
        if 'price' in args:
            self.price = args.get('price')
        if 'company' in args:
            self.company = args.get('company')


    def info(self):
        if 'name' in self.__dict__:
          print(f'자동차명: {self.name} ', end="\t")
        if 'price' in self.__dict__:
          print(f'가격: {self.price}', end="\t")
        if 'company' in self.__dict__:
          print(f'회사: {self.company}', end="\t")


c = Car(name='그랜저', price='4000', company='현대')
c2 = Car(name='모닝', price='2100')

c.info()
c2.info()
print(c.addr)
print(c2.addr)
#c2.addr = '부산' # 올바른방식은  Class 명 . 으로 접근해야한다
