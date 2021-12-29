import tensorflow as tf
from keras.api._v2 import keras
from keras.api._v2.keras.layers import Input, Dense, Conv2D, MaxPooling2D, AveragePooling2D, Flatten, BatchNormalization, Activation


class CM_block(keras.layers.Layer):

    """
    Conv2D + Maxpooling2D는 자주 쓰는 layer 조합이므로 이를 하나의 클래스로 묶어 보고자 합니다.
    CM (conv + maxpooling) block에 필요한 parameters는
    (1) Conv2D.__init__(filters, kernel_size)이므로 filters, kernel_size가 우선 필요하구요
    (2) 만약 CM block이 처음에 사용되면 input_shape이 필요합니다.

    example:
    x = tf.ones((64, 28, 28, 1))
    cm = CM_block(32, 3, input_shape=(28, 28, 1))
    cm.weights  >>> []
    y = cm(x)
    cm.weights >>>  [<tf.Variable 'cm_block_6/kernel:0' shape=(3, 3, 1, 32) dtype=float32, ...]
    print(y.shape)

    """

    def __init__(self, filters, kernel_size, *args, **kwargs):
        super().__init__()
        self.conv = Conv2D(filters=filters,
                           kernel_size=kernel_size,
                           *args, **kwargs)
        self.maxp = MaxPooling2D()

    def call(self, inputs, **kwargs):
        x = self.conv(inputs)
        outputs = self.maxp(x)
        return outputs



class IdentityBlockConv(keras.layers.Layer):
    def __init__(self, filters, kernel_size, is_same_filters):
        super().__init__()

        self.filters = filters
        self.kernel_size = kernel_size
        self.is_same_filters = is_same_filters

        if not self.is_same_filters:
            self.conv_0 = Conv2D(self.filters, 1, strides=2)
        self.conv_1 = Conv2D(self.filters, self.kernel_size, padding='same')
        self.batch_1 = BatchNormalization()
        self.act_1 = Activation(tf.nn.relu)

        self.conv_2 = Conv2D(self.filters, self.kernel_size, padding='same')
        self.batch_2 = BatchNormalization()
        self.act_2 = Activation(tf.nn.relu)

    def call(self, inputs):
        if not self.is_same_filters:
            inputs = self.conv_0(inputs)
        x_skip = tf.identity(inputs)

        x = self.conv_1(inputs)
        x = self.batch_1(x)
        x = self.act_1(x)

        x = self.conv_2(x)
        x = self.batch_2(x)
        x = self.act_2(x)

        x = x + x_skip
        return tf.nn.relu(x)

# class ResNetBlockFromScratch(keras.layers.Layer):
#     def __init__(self, num_classes, **kwargs):
#         super().__init__(**kwargs)
#         self.num_classes = num_classes
#
#     def build(self, input_shape):
#         self.units = input_shape[-1]
#         self.w = self.add_weight(
#             shape=(self.units, self.units),
#             initializer=tf.random_normal_initializer(),
#             trainable=True
#         )
#
#         self.b = self.add_weight(
#             shape=(self.units,),
#             initializer=tf.zeros_initializer(),
#             trainable=True
#         )
#
#         self.w2 = self.add_weight(
#             shape=(self.units, self.units),
#             initializer=tf.random_normal_initializer(),
#             trainable=True
#         )
#
#         self.b2 = self.add_weight(
#             shape=(self.units,),
#             initializer=tf.zeros_initializer(),
#             trainable=True
#         )
#
#     def call(self, inputs, *args, **kwargs):
#         x = tf.matmul(inputs, self.w1)
#         x = tf.nn.bias_add(x, self.b1)
#         x = tf.nn.relu(x)
#         x = tf.matmul(x, self.w2)
#         x = tf.nn.bias_add(x, self.b2)
#         x = x + inputs
#         x = tf.nn.relu(x)
#         return x