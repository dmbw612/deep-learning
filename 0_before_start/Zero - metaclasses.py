# https://tech.ssut.me/understanding-python-metaclasses/
class ObjectCreator:
    pass
obj1 = ObjectCreator()
obj2 = ObjectCreator()

print('NAME:{}, TYPE:{}, PRINT:{}'.format(ObjectCreator.__name__, type(ObjectCreator), ObjectCreator))
print('TYPE:{}, PRINT:{}'.format(type(obj1), obj1))
print('TYPE:{}, PRINT:{}'.format(type(obj2), obj2))
# <__main__.ObjectCreator object at 0x0000023095027F88>
# class 키워드를 사용할 때 python은 실행하면서 객체를 만들어 냅니다.
# 위 코드는 myClass라는 이름의 객채를 만들어냅니다.

def echo(o):
    print(o)
echo(ObjectCreator) # 클래스를 함수의 인자로 넘길 수 있습니다.
# <class '__main__.ObjectCreator'>
print(hasattr(ObjectCreator, 'new_attribute'))
# False
ObjectCreator.new_attribute = 'foo' # 클래스에 새로운 속성을 추가할 수 있습니다.
print(hasattr(ObjectCreator, 'new_attribute'))
# True
print(ObjectCreator.new_attribute)
# foo
ObjectCreatorMirror = ObjectCreator # 클래스를 변수에 할당할 수 있습니다.
print(ObjectCreatorMirror.new_attribute)
# foo
print(ObjectCreatorMirror())
# <__main__.ObjectCreator object at 0x8997b4c>

# class를 직접 만들 수 있습니다.
# 왜냐하면 type(class)를 출력해보면 <class 'type'>이라고 나오기 때문에 이것이 type으로 생성됨을 알 수 있고
# type은
# type(name of the class,
#      tuple of the parent class (for inheritance, can be empty),
#      dictionary containing attributes names and values)로 쓰일 수 있기 때문입니다.

ObjectCreator_createdbyType = type('ObjectCreator', (), {})
print('NAME:{}, TYPE:{}, PRINT:{}'.format(ObjectCreator_createdbyType.__name__, type(ObjectCreator_createdbyType), ObjectCreator_createdbyType))
print('NAME:{}, TYPE:{}, PRINT:{}'.format(ObjectCreator.__name__, type(ObjectCreator), ObjectCreator))

### 그렇다면 class를 만드는 객체는 무엇일까요? type을 만드는 객체는 또 무엇일까요? 상위의 무엇인가가 얘네들을 만들텐데 말이죠.
# metaclass는 클래스를 만드는 '그 무언가'입니다.
# type은 builtins.py 모듈 내의 type Class로 정의됩니다.

# 모든 것, Python에서의 모든 것은 객체입니다. 여기에는 정수, 문자열, 함수, 클래스를 포함합니다. 이 모든 것들은 객체입니다. 그리고 이 모든 것들은 클래스로부터 생성됩니다:
age, name = 35, 'john'
def func(): pass
class cls(): pass
print(age.__class__, name.__class__, func.__class__, cls().__class__)
print(age.__class__.__class__, name.__class__.__class__, func.__class__.__class__, cls().__class__.__class__)
# <class 'type'> <class 'type'> <class 'type'> <class 'type'>