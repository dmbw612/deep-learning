# https://hyun-am-coding.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8D%B0%EC%BD%94%EB%A0%88%EC%9D%B4%ED%84%B0

""" 먼저 기본적인 데코레이터는 호출 가능 객체를 입력받아 다른 호출 가능 객체를 반환하는 호출 가능한 하나의 함수이다.
    ( ... 호출 가능한 객체이다.)"""

# 1. 가장 간단한 데코레이터입니다. null_decorator는 호출 가능하며, 다른 호출 가능 객체를 입력으로 받아
# 그 호출 가능 객체를 수정하지 않고 반환합니다.
def null_decorator(func):
    return func

def greet():
    return "Hello!"
greet = null_decorator(greet)
print(greet())

@null_decorator
def greet():
    return "Hello!"
print(greet())
# @ 구문을 사용하면 정의 시간에 즉시 함수가 장식됩니다. 이로 인해 까다로운 해킹만 하지 않으면 장식되지 않은 원본에
# 접근하기가 어려워 집니다. 만약 원본을 사용하고 싶으면, @ 구문을 사용하지 않고 직접 장식하면 됩니다.

# 2. 데코레이터를 통한 동작 수정하기
def lowercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.lower()
        return modified_result
    return wrapper
# lowercase는 callable한 function을 받아서 수정된 wrapper function을 반환하는 데코레이터이다.
# lowercase 데코레이터가 잘 작동되는지 살펴보자.
@lowercase
def greet():
    return "Hello!"
print(greet())
# 출력값이 소문자로 잘 변경된 것을 확인할 수 있습니다.

# 이제 두개의 데코레이터를 만들어서 데코레이터가 중복으로 함수에 적용되는지 확인하겠습니다.
def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def emphasize(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper

@strong
@emphasize
def greet():
    return "Hello!"
print(greet())
# <strong><em>Hello!</em></strong>가 출력되는 것을 보니 아래부터 순서대로 데코레이터가 적용됨을 확인할 수 있습니다.
# 이것은 decorated_greet = strong(emphasize(greet))과 동일하게 작동합니다.
# 계속 callable한 객체를 입력으로 받아 출력하는 것을 볼 수 있습니다.

# 3. 인자를 받는 함수 장식하기
# 가변적인 인자 *args, **kwargs를 받는 함수를 데코레이터 처리해봅시다.

def proxy(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
# wrapper 클로저 정의에서 *및 ** 연산자를 사용하여 모든 위치 및 키워드 인자를 수집하고 변수(args와 kwargs)에 저장합니다.
# wrapper 클로저는 수집된 인자를 * 및 ** '인자풀기' 연산자를 사용하여 원래 입력 함수로 전달합니다.

# 이제 proxy 데코레이터에 의해 적용된 기술을 좀 더 유용한 실제 예제로 확장하겠습니다. 다음은 함수 인자와 결과를 기록하는
# trace 데코레이터입니다.

def trace(func):
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() returned {original_result}')
        return original_result
    return wrapper

@trace
def say(name, line):
    return f'{name}: {line}'
print(say('John', 'Hello World!'))
# TRACE: calling say() with ('John', 'Hello World!'), {}
# TRACE: say() returned John: Hello World!
# John: Hello World!

# 디버깅을 위해서 꼭 해야할 일!
def lowercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.lower()
        return modified_result
    return wrapper
@lowercase
def greet():
    return "Hello!"
decorated_greet = greet()
print(greet.__name__)
# wrapper가 출력되는 현상이 발생해서 디버깅이 어려움. 따라서 아래와 같이 습관적으로 하면 좋음.

import functools
def lowercase(func):
    @functools.wraps(func)
    def wrapper():
        original_result = func()
        modified_result = original_result.lower()
        return modified_result
    return wrapper
@lowercase
def greet():
    return "Hello!"
decorated_greet = greet()
print(greet.__name__)

