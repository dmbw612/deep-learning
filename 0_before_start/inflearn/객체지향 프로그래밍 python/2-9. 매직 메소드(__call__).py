"""
# 매직 메서드 __str__을 customize함.
callable한 인스턴스 만들기.. 드디어 내가 궁금했던 것을 찾았다..
droid1이 호출되기 위해서는 droid를 만드는 상위 class에 무조건 __call__함수가 있어야 하는 것이다.
즉, 호출 가능한 객체를 만들기 위해서는 매직 매서드 __call__이 있는 클래스를 사용해야 한다.
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
    def is_this_robot_class():
        print('이것은 Robot 클래스입니다.')

    # 매직 메서드 __str__을 customize함.
    def __str__(self):
        return f'It\'s {self.name} robot!!'

    def __call__(self):
        print(f"{self.name} is callable")
        return f"{self.name} is callable"

droid1 = Robot('R2-D2')
droid1.say_hi()

print(droid1)
print(droid1.__str__()) # <__main__.Robot object at 0x00000196C6BA0E80>

droid1() # TypeError: 'Robot' object is not callable
"""
droid1이 호출되기 위해서는 droid를 만들 상위 class에 무조건 __call__함수가 있어야 하는 것이다.
"""
