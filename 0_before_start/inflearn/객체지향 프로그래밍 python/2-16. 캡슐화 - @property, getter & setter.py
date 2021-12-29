"""
숨겨진 __속성을 읽기 위해서
@property를 사용하여 __속성에만 접근할 수 있는 새로운 메서드를 생성한다.

@property
def 속성(self):
    return self.__속성

이때 print(Robot.속성)은 잘 실행이 되는데
이는 속성에 접근만 수 있는 getter가 작동되기 때문에 가능한 것이고
새로운 값을 설정할 수는 없다.


"""



class Robot:

    """
    Robot class
    """

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

droid = Robot('R2-D2', 2)

print(droid.age)
# droid.age = 10 #AttributeError: can't set attribute

droid.age += 1
print(droid.age)
print(droid.name)
print(dir(droid))
print(droid)
print(Robot)
