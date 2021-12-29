def copyright(func):

    # 새로운 함수를 재정의합니다.
    def new_func():
        print("(c)dmbw612")
        func()

    return new_func

@copyright
def smile():
    print("smile")

@copyright
def angry():
    print("angry")

@copyright
def love():
    print("love")

@copyright
def sad():
    print("sad")

@copyright
def fear():
    print("fear")

@copyright
def hesitate():
    print("hesitate")

@copyright
def nervous():
    print("nervous")

@copyright
def sleepy():
    print("sleepy")

# smile = copyright(smile)
# angry = copyright(angry)
# love = copyright(love)
# sad = copyright(sad)
# fear = copyright(fear)
# hesitate = copyright(hesitate)
# nervous = copyright(nervous)
# sleepy = copyright(sleepy)

smile()
angry()
love()
sad()
fear()
hesitate()
nervous()
sleepy()
