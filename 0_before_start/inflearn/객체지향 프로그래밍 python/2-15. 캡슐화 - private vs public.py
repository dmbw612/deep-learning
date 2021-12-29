"""
public과 private의 구분에 대해서 설명한다.
외부에서 instance 내부 네임스페이스로 접근하지 못하도록 해야지.
이것을 바로 private이라고 합니다. private 변수, private 메서드

짝대기 두개 쓰면 __ 접근을 못한다.

"""

class Robot:

    """
    Robot class
    """

    population = 0

    def __init__(self, name, age):
        self.name = name
        self.__age = age # private 변수로 바꾸는 방법이 __ 붙이는 것임. 이것을 은닉이라고 함.
        Robot.population += 1

    def say_hi(self):
        # 알고리즘 생략
        print(f"안녕하세요. 저는 Robot-class {self.name}입니다")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        print(f'만들어진 robot 개수는 {cls.population}개 입니다.')

ss = Robot('yss', 8)
print(ss.__age)