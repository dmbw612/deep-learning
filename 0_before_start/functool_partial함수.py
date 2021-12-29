def power(base, exponent):
    return base ** exponent

def squre(base):
    return power(base, 2)

def cude(base):
    return power(base, 3)

# 그렇다면 100개를 만들어야 한다면...?

import functools
squre = functools.partial(power, exponent=2)