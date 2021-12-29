"""
func2
self : <__main__.SelfTest object at 0x000001F55D7177C0>
class안의 self 주소 :  1916570269632

func1
cls: <class '__main__.SelfTest'>

인스턴스의 주소 :  1916570269632
"""


class SelfTest:

    name = 'dmbw612' # 클래스 변수

    def __init__(self, x):
        self.x = x # 인스턴스의 네임스페이스 안에 x를 존재하게 함.

    @classmethod
    def func1(cls):
        print('func1')
        print(f'cls: {cls}')
        print('')

    def func2(self):
        print('func2')
        print(f'self : {self}')
        print('class안의 self 주소 : ', id(self))

test_object = SelfTest(17)

test_object.func2()
SelfTest.func1()

print('인스턴스의 주소 : ', id(test_object))