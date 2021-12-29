"""
객체를 부품화 할 수 있다.
"""

class Robot:
    population = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age # private 변수로 바꾸는 방법이 __ 붙이는 것임. 이것을 은닉이라고 함.
        self.x = 0
        Robot.population += 1

    @property
    def name(self):
        return f'dmbw612 {self.__name}'

    @property #외부에서 접근한 속성에 대해서 반응할 수 있게 해줌. 그 반응을 변형시킬수도 있음.
    def age(self):
        return self.__age

    @age.setter # __속성에 접근하여 기존의 self.__속성값을 외부에서 입력된 새로운 속성값으로 바꿀 수 있도록 한다.
    def age(self, new_age):
        if new_age < 0:
            raise TypeError("invalid range to age")
        else:
            self.__age = new_age

    def say_hi(self):
        print(f"안녕하세요. 저는 Robot-class {self.__name}입니다")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        print(f'만들어진 robot 개수는 {cls.__population}개 입니다.')

class Siri(Robot):

    def __init__(self, name, age):
        super().__init__(name, age)

    def say(self):
        print("hello apple")


class Bixby(Robot):

    def __init__(self, name, age):
        super().__init__(name, age)

    def say(self):
        print("안녕하세요.")


class BixbyCal:

    def __init__(self, name, age):
        self.Robot = Robot(name, age)

    def cal_add(self, a, b):
        return self.Robot.cal_add(a, b)
