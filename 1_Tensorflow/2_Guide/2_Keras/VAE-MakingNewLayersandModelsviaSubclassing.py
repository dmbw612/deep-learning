import tensorflow as tf
from keras.api._v2 import keras

class LinearWithoudBuild(keras.layers.Layer):
    """
    A layer encapsulates both the layer's weights and
    a transformation from inputs to outputs (a 'call', the layer's foward pass).
    """
    def __init__(self, input_dim, output_units):
        super().__init__()
        w_init = tf.random_normal_initializer()
        self.w = tf.Variable(
            initial_value=w_init(shape=(input_dim, output_units)),
            trainable=True
        )

        b_init = tf.zeros_initializer()
        self.b = tf.Variable(
            initial_value=b_init(shape=(output_units,)),
            trainable=True
        )

    def call(self, inputs, *args, **kwargs):
        return tf.matmul(inputs, self.w) + self.b

x = tf.ones(shape=(2, 2))
linear = LinearWithoudBuild(input_dim=x.shape[1], output_units=4)
y = linear(x)
assert linear.weights == [linear.w, linear.b] # assert는 정확하게 확인한다.



class Linear(keras.layers.Layer):
    def __init__(self, output_units):
        super().__init__()
        self.output_units = output_units

    def build(self, input_shape):
        self.w = self.add_weight(
            shape=(input_shape[-1], self.output_units),
            initializer=tf.random_normal_initializer(),
            trainable=True
        )

        self.b = self.add_weight(
            shape=(self.output_units,),
            initializer=tf.zeros_initializer(),
            trainable=True
        )

    def call(self, inputs, *args, **kwargs):
        return tf.matmul(inputs, self.w) + self.b

# At instantiation, we don't know on what inputs this is going to get called
# The layer's weights are created dynamically the first time the layer is called
linear = Linear(output_units=7)
y = linear(x)

class MLPBllock(keras.layers.Layer):
    def __init__(self):
        super().__init__()
        self.linear_1 = Linear(16)
        self.linear_2 = Linear(32)
        self.linear_3 = Linear(1)

    def call(self, inputs, *args, **kwargs):
        x = self.linear_1(inputs)
        x = tf.nn.relu(x)
        x = self.linear_2(x)
        x = tf.nn.relu(x)
        return self.linear_3(x)

mlp = MLPBllock()
x = tf.ones(shape=(3, 100))
y = mlp(x)

class CustomDropout(keras.layers.Layer):
    def __init__(self, rate, *args, **kargs):
        super().__init__(*args, **kargs)
        self.rate = rate

    def call(self, inputs, trianing=None, *args, **kwargs):
        if trianing:
            return tf.nn.dropout(inputs, rate=self.rate)
        return inputs


class ResNet(keras.models.Model):
    def __init__(self, num_classes=1000):
        super().__init__()
        self.block_1 = ResNetBlock

from keras.layers import ResNet