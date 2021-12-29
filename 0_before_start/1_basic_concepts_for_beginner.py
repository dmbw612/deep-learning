import init
# 그냥 import init 하면, init 패키지가 실행되기는 하는데, init만 네임스페이스에 저장된다.
# 따라서 init 패키지 안의 __init__.py 모듈에서 import 된 패키지들을 사용할 수가 없다.
# 따라서 init 패키지 안의 __init__.py 모듈에서 import 된 패키지들을 그대로 import한다.
from init import *
print(dir()) #네임스페이스에서 무엇이 있는지 살표보면, __init__.py 모듈 내에서 import 된 패키지들이 저장된 것을 확인할 수 있다.

# keras의 layers의 위치를 알아보자.
print(keras.layers)

import keras.layers.Layer
# 실패한다. 그러므로 class를 바로 import할 수는 없구나. 이게 성공하려면 Layer.py가 있어야 한다.
# 그런데 아래는 성공한다.
from keras.layers import Layer
print(Layer)
# <class 'keras.engine.base_layer.Layer'>
# 사실 keras.layers 폴더 안에 __init__.py 모듈을 보면
# from keras.engine.base_layer import Layer 이렇게 실행이 되도록 한다.
# 따라서 우리가 from 패키지 import 클래스라고 치면, 패키지의 __init__.py이 실행된 뒤 그 상황에서 클래스를 불러 올 수 있는 것 같다.
# 여기서 Layer class는 keras.layers 폴더 안에 있는 Layer.py가 아니라 그냥 __init__.py 안에서 불러오는 Layer 클래스다.

# 그리고 from keras.layers import * 해도 되는데 그럼 네임스페이스에 너무 많은

dir()

import sys