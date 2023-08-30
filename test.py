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
