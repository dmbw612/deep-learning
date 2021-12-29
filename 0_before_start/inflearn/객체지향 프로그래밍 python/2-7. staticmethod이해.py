"""
클래스 안에서 self, cls와 상관없는 메서드를 만들 때
그냥 def 하면 cls.method로만 접근이 가능하다.

@staticmethod를 이용하면
instance.method로도 접근이 가능하기 때문에 @staticmethod를 사용한다.

"""

siri_name = "siri"
siri_code = 120397615
jarvis_code = 31312345
bixby_code = 10958623
def siri_say_hi():
    # algorithm omitted
    print("안녕 내 이름은 시리야")

def siri_add_cal(a, b):
    return a + b

def siri_die():
    # algorithm omitted
    print("종료합니다.")

# Robot이라는 class를 정의하면, Robot이라는 이름의 독립적인 네임스페이스가 생기는데 여기에
# 클래스와 관련된 속성과 메서드가 저장되므로, Robot.population과 같이 클래스 내의 변수에 접근할 수 있는 것이다.
class Robot:

    """
    [Robot class]
    Author: dmbw612
    Role: 아직 미정이에요.
    """

    # 클래스 변수 (인스턴스들이 공유하는 변수)
    population = 0

    # 생성자 함수
    def __init__(self, name, code):
        self.name = name # 인스턴스 변수
        self.code = code
        Robot.population += 1

    # 인스턴스 메서드
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

siri = Robot('siri', siri_code)
jarvis = Robot('jarvis', jarvis_code)

siri.is_this_robot_class()