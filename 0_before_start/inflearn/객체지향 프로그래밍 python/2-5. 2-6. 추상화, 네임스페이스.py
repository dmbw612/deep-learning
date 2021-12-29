"""
인스턴스 네임스페이스에 인스턴스 메서드가 없음에도 실행이 가능한 이유는
특정 인서턴스 메서드를 실행시켰을 때
인스턴스 네임스페이스에서 해당 인스턴스 메서드가 발견되지 않으면
클래스 네임스페이스에서 해당 인스턴스 메서드를 찾기 때문이다.

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



siri = Robot('siri', siri_code)
jarvis = Robot('jarvis', jarvis_code)
bixby = Robot('bixby', bixby_code)
siri.say_hi()
jarvis.say_hi()

Robot.how_many()

print(Robot.__dict__)
print(siri.__dict__)
print(jarvis.__dict__) # 인스턴스 네임스페이스인데도 불구하고 인스턴스 메서드는 들어가 있지 않다.

print(siri.population) # 인스턴스를 통해서도 클래스 변수에 접근가능하다.

print("")
Robot.say_hi(siri)
siri.say_hi()

print('siri에서 사용 가능한 속성/메서드:', dir(siri))
print('class의 주석은', Robot.__doc__)
print('인스턴스가 어떤 class로 만들어진 건지 궁금하면', siri.__class__)