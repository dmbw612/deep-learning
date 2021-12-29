"""
https://jins-sw.tistory.com/30
이분 블로그 좋다.
"""

def f(a,b,c):
    print(a, b, c)

# 아래에서 1, 2는 positional arguments이고 c=3은 인자의 이름을 명시했기 때문에 keywword arguments입니다.
# keyword arguments는 항상 positional arguments 다음에 나와야 합니다.
f(1,2,c=3)

# parameters는 함수를 선언할 때 사용한 것들이고, arguments는 실제로 이 함수를 호출할 때 사용하는 것들입니다.
# 다시 *args, **kwargs 이야기로 돌아오겠습니다. *args는 미리 정해지지 않은 positional arguments를 받을 때 사용합니다.
# *args는 list 형태로입니다.
# *args가 가변적인 positional arguments를 담기 위해서 쓰인다면, **kwargs는 가변적인 keyword arguments를 담기 위해서 쓰입니다.
# kwargs의 kw는 keyword를 의미합니다. 물론 kwargs도 일반적인 변수이기 때문에 아무 이름이나 사용할 수 있습니다.
