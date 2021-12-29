class Calculator:
    # 생성자. 메모리에 올라가서 instance를 만드는 순가 즉시 실행.
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


cal1 = Calculator(1, 2)

print(cal1.a)
print(cal1.add())

#인스턴스는 개별적인 네임스페이스를 가진다.