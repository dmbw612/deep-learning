"""
https://hcnoh.github.io/2019-01-30-python-namespace
"""


# namespace_example01.py
def outer_func():
    a = 20

    def inner_func():
        a = 30
        print("a = %d" % a)

    inner_func()
    print("a = %d" % a)


a = 10
outer_func()
print("a = %d" % a)


# namespace_example01.py
def outer_func():
    a = 20

    def inner_func():
        a = 30
        print('namesapce1', locals())

    inner_func()
    print('namesapce2', locals())


a = 10
outer_func()
print('namesapce3', locals())