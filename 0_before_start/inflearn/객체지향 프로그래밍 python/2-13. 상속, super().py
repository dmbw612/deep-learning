"""
오버라이딩!
super은 상위 class를 불러오는 거니까
overriding을 위해서 한다고 대충 생각하자.
그러니까 overriding하는 거 아니면 super쓸 필요 없이 self로 써서 의미상 잘 전달되게 하자.


"""

class Robot:

    """
    [Robot class]
    Author: dmbw612
    Role: 아직 미정이에요.
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

    def die(self):
        print(f"{self.name}은 종료됩니다.")

    @classmethod
    def how_many(cls):
        print(f'만들어진 robot 개수는 {cls.population}개 입니다.')

    # self, cls가 없는 함수도 필요하자나?
    @staticmethod
    def are_you_robot():
        print('나는 Robot입니다..')

    # 매직 메서드 __str__을 customize함.
    def __str__(self):
        return f'It\'s {self.name} robot!!'

    def __call__(self):
        print(f"{self.name} is callable")
        return f"{self.name} is callable"

class Siri(Robot):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def say_hi(self): # 오버라이딩 함.
        # 알고리즘 생략
        print(f"안녕하세요. 저는 Siri-class {self.name}입니다")

    def call_me(self):
        print("네? 시리입니다. 말씀하세요.")

    def cal_mul(self, a, b):
        return a * b

    def cal_flexible(self, a, b):
        super().say_hi()
        self.say_hi()
        return self.cal_mul(a, b) + self.cal_add(a, b)

    @classmethod
    def hello_apple(cls):
        print(cls, 'hello apple!!')

siri = Siri('iphone8', 17)
print(siri.name, siri.age)
print(siri.cal_flexible(10, 20))

"""
Python 2.

class A:
    def __init__(self):
        pass
        
class B(A):
    def __init__(self):
        super(B, self).__init__()

"""