"""
mro()는 상속의 관계를 보여주는 method
"""

class Robot(object):

    """
    Robot class
    """

    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1

    def say_hi(self):
        # 알고리즘 생략
        print(f"안녕하세요. 저는 Robot-class {self.name}입니다")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        print(f'만들어진 robot 개수는 {cls.population}개 입니다.')

class Siri(Robot):
    def call_me(self):
        print("네? 시리입니다. 말씀하세요.")

    def cal_mul(self, a, b):
        return a * b


siri = Siri('iphone8')

print(Siri.mro()) # mro()는 상속의 관계를 보여주는 method
# [<class '__main__.Siri'>,
#  <class '__main__.Robot'>,
#  <class 'object'>]

print(object)
print(dir(object))
print(object.mro())
print(int.mro())
