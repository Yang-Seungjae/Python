from abc import *

class TV(metaclass=ABCMeta) :

    @abstractmethod
    def power_on(self):
        pass

class LGTV(TV):
    def power_on(self):
        print('power on')

# LGTV() 파이썬은 실행하기전까지 에러를 잡을수없다 클래스를 만든것만으로는 에러가 발생안함 인터프리터방식이기때문

tv = LGTV()
tv.power_on()