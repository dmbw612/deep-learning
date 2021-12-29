"""
오버라이딩!
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
        print(f"안녕하세요. 저는 {self.name}입니다")

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
        self.name = name
        self.age = age
        Siri.population += 1
    def call_me(self):
        print("네? 시리입니다. 말씀하세요.")

    def cal_mul(self, a, b):
        return a * b

    @classmethod
    def hello_apple(cls):
        print(cls, 'hello apple!!')

siri = Siri('iphone8', 17)
siri.how_many()