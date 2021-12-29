"""
on this page:
(1) Layers: common sets of useful operations
(2) Implementing custom layers
(3) Models: Composing layers
"""

""" 
from tensorflow import keras로 하면 layers에 접급이 안됩니다.
따라서 tensorflow.keras import layers로 해야합니다.
한 번 해보시면 아시게 될 것입니다.
"""
import tensorflow
import tensorflow as tf
from tensorflow.keras import layers
print(tf.config.list_physical_devices('GPU'))


"""
tensorflow.keras.layers는 module입니다. [https://www.tensorflow.org/api_docs/python/tf/keras/layers]
이 모듈 안에 우리가 사용하고 싶은 Dense, Conv2D 등 많은 것들이 있습니다.
이 layers 모듈 안에 Dense, Conv2D 등은 class로 정의되어 있어
객체선언을 통해 사용할 수 있습니다.


layers.Dense()를 통해 instantce가 생성될 수 있습니다.
>>> layers.Dense()
TypeError: __init__() missing 1 required positional argument: 'units' 라는 error가 뜨게 됩니다.
Dense에 units라는 argument가 필수인 듯 합니다.

@keras_export('keras.layers.Dense')
class Dense(Layer):
  def __init__(self, units,...)

units는 필수 argument인 것을 확인할 수 있습니다.
"""
layer = layers.Dense(units=10)

"""
>>> layer
<keras.layers.core.Dense object at 0x00000189349E7C08>
layer를 출력해보면 Dense object임을 확인할 수 잇습니다.

"""

"""
Dense라는 class는 Layer class를 상속합니다.

def class Dense(Layer): 
  `Dense` implements the operation:
  `output = activation(dot(input, kernel) + bias)`
  where `activation` is the element-wise activation function passed as the 
  `activation` argument, 
  `kernel` is a weights matrix created by the layer, and 
  `bias` is a bias vector created by the layer(only applicable if `use_bias` is `True`). 
  These are all attributes of `Dense`.

  Note: If the input to the layer has a rank greater than 2, then `Dense`
  computes the dot product between the `inputs` and the `kernel` along the
  last axis of the `inputs` and axis 0 of the `kernel` (using `tf.tensordot`).
  For example, if input has dimensions `(batch_size, d0, d1)`,
  then we create a `kernel` with shape `(d1, units)`, and the `kernel` operates
  along axis 2 of the `input`, on every sub-tensor of shape `(1, 1, d1)`
  (there are `batch_size * d0` such sub-tensors).
  The output in this case will have shape `(batch_size, d0, units)`.

  self.kernel = self.add_weight(
    'kernel',
    shape=[last_dim, self.units],
    initializer=self.kernel_initializer,
    regularizer=self.kernel_regularizer,
    constraint=self.kernel_constraint,
    dtype=self.dtype,
    trainable=True)

아직 self.kernel은 생성되지 않은 시기입니다. kernel은 weights를 의미합니다.

>>> layer.kernel
AttributeError: 'Dense' object has no attribute 'kernel'
>>> layer.input_shape
AttributeError: The layer has never been called and thus has no defined input shape.

이라는 것을 보니 객체화 된 layer를 호출해야 할 것 같습니다.
그리고 call하기 위해서 어떤 것이 주어져야 하는지 좀 살펴봅니다.

def call(self, inputs):

이렇게 정의되어 있네요.
그럼 layer 객체를 inputs를 입력하여 호출하겠습니다.
"""
outputs = layer(inputs=tf.ones([2,5]))
"""
layer에 3 by 10 크기의 tf.ones를 입력으로 넣었는데,
layer.call(iputs)는 output을 return 했습니다. 
layer 객체에는 무슨 변화가 있을까요?

>>> layer.kernel
<tf.Tensor: shape=(2, 10), dtype=float32, numpy=
array([[-0.23161638,  0.6509664 , -0.5396638 ,  0.10030735,  0.21620187,
        -0.3369079 ,  0.22502735, -0.3635285 , -0.16091165, -0.21287507],
       [-0.23161638,  0.6509664 , -0.5396638 ,  0.10030735,  0.21620187,
        -0.3369079 ,  0.22502735, -0.3635285 , -0.16091165, -0.21287507]],
      dtype=float32)>
>>> layer.built
Ture

layer에는 자기 상태(weight)가 새로 생겨나고, kernel이라는 이름에 그 값이 저장되어 있습니다. 
layer가 build 메소드를 실행했으면 self.built=True가 되는데, 이를 layer.built로 확인해보니 잘 실행되었네요.
"""

layer.variables
layer.trainable_variables
layer.kernel
layer.bias

"""
layer의 weighs, bias는 위와 같이 접근하고 확인해볼 수 있습니다.
얘네 들이 대체 어디서 생성되었는지는 찾기 어렵네요..
아무튼 나중에 그 실마리를 찾기 바라면서, 다음으로 진행해 보죠.
"""

"""
==================================== Implementing custom layers ====================================
(1) __init__
(2) build
(3) call

우리가 layer를 instantiate할 때,
__init__에서 하면, weights를 정의하기 위해 input data를 알아야 한다. 하지만,
build에서 하면, weight는 나중에 정의할 수 있기 때문에 graph구조를 먼저 만다는 keras의 idea에 build에서 
weight가 초기화 되는 것이 실용적이고 idea 측면에서도 적합하다고 생각한다.
"""

from tensorflow.keras.layers import Layer
class MyDenseLayer(Layer):
    def __init__(self, units):
        super().__init__() # 왜 super(MyDenseLayer, self).__init__()하는지 알 수가 없다.
        self.num_outputs = units
    def build(self, input_shape):
        last_dim = int(input_shape[-1])
        self.kernel = self.add_weight(name="kernel",
                                      shape=[last_dim, self.num_outputs])
    def call(self, inputs):
        outputs = tf.matmul(inputs, self.kernel)
        return outputs

layer = MyDenseLayer(units=10)
outputs = layer(tf.ones([2,5]))
print([var.name for var in layer.trainable_variables])

"""
==================================== Models: Composing layers ====================================
For example, each residual block in a resnet is a composition of 
convolutions, batch normalizations, and a shortcut. 
Layers can be nested inside other layers.
"""

from tensorflow.keras import Model # Model은 class입니다.
class ResnetIdentityBlock(Model):
    def __init__(self, filters, kernel_size):
        super().__init__(name='')
        filters1, filters2, filters3 = filters

        self.conv2a = layers.Conv2D(filters1, (1,1))
        self.bn2a = layers.BatchNormalization()

        self.conv2b = layers.Conv2D(filters2, kernel_size, padding='same')
        self.bn2b = layers.BatchNormalization()

        self.conv2c = layers.Conv2D(filters3, (1,1))
        self.bn2c = layers.BatchNormalization()

    def call(self, input_tensor, training=False):
        x = self.conv2a(input_tensor)
        x = self.bn2a(x, training=training)
        x = tf.nn.relu(x)

        x = self.conv2b(x)
        x = self.bn2b(x, training=training)
        x = tf.nn.relu(x)

        x = self.conv2c(x)
        x = self.bn2c(x, training=training)

        x += input_tensor
        return tf.nn.relu(x)

block = ResnetIdentityBlock([1,2,3], 1)
outputs = block(tf.ones([1, 2, 3, 3]))
for layer in block.layers:
    print(layer)

block.summary()