#상속관련

class Parent:

    def __init__(self):
        self.name = '부모'
        print('parent 호출..')


    def info(self):
        print('Parent info() 호출...')

class Child(Parent): # 상속개념
    def __init__(self):
        super().__init__() # 부모생성자 만들기  호출하기
        print('child 호출..')
    def info(self):
        super().info() # 부모에 있는 info 메소드를 호출하고싶다면
        print('child info() 호출')


# p = Parent()
p = Child()
p.info()
# 부모와 자식에 같은 메소드가 있어도 자식의 메소드가 우선시된다
print(p.name) # 상속해도 파이썬에서는 자동으로 부모의 생성자를 호출하지 않음 ==> 에러발생 자식 생성자에서 부모생성자를 호출해줘야함
