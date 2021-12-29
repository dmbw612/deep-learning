import sys

import tensorflow as tf
from keras.api._v2 import keras

for p in sys.path:
    print(p)

print("")
print('python\t\t', sys.version)
print('tensorflow\t', tf.__version__)
print('keras\t\t', keras.__version__)
