"""
객체 내에 있는 변수들은 __dict__를 통해서 관리가 된다.
__slots__를 통한 변수 관리.

"""

class WithouSlotClass:

    def __init__(self, name, age):
        self.name = name
        self.age = age


wos = WithouSlotClass("dmbw612", 30)
for i, attr in enumerate(dir(wos)):
    print(i, attr)
print(wos.__dict__)


wos.__dict__["word"] = "hello. World!"
print(wos.__dict__)


class WithSlotClass:
    __slots__ = ['name', 'age'] # 사용 가능한 변수를 제한함.dict를 사용하지 않음.

    def __init__(self, name, age):
        self.name = name
        self.age = age


ws = WithSlotClass('dmbw612', 30)

print(ws.__dict__)
print(ws.__slots__)

import timeit

#* 메모리 사용량 비교
def repeat(obj):
    def inner():
        obj.name = "dmbw612"
        obj.age = 30
        del obj.name
        del obj.age

    return inner

use_slot_time = timeit.repeat(repeat(ws), number=999999)
no_slot_time = timeit.repeat(repeat(wos), number=999999)

print('use slot', min(use_slot_time))
print('no slot', min(no_slot_time))