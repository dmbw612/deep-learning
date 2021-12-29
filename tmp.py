import tensorflow as tf
from keras.api._v2 import keras


class CM_block(keras.layers.Conv2D):

    """
    Conv2D + Maxpooling2D는 자주 쓰는 layer 조합이므로 이를 하나의 클래스로 묶어 보고자 합니다.
    CM (conv + maxpooling) block에 필요한 parameters는
    (1) Conv2D.__init__(filters, kernel_size)이므로 filters, kernel_size가 우선 필요하구요
    (2) 만약 CM block이 처음에 사용되면 input_shape이 필요합니다.
    (3) filters, kernel_size는 positional argument이고, input_shape keyward argument로만 강제적으로 사용하기 위하여 그들 사이에 * 를 삽입하였습니다.
    """

    def __init__(self, filters, kernel_size, input_shape=None):
        super().__init__(filters=filters,
                         kernel_size=kernel_size,
                         input_shape=input_shape)
        """
        Conv2D의 super()인 CONV에서 이미 self.filters = filters를 사용하여 클래스 속성을 정의하였으므로 self 따위를 적을 필요가 없습니다.
        다만, super().__init__()에는 넣어줘야 가장 최 상단에서 self.속성 = 속성이 정의됩니다.
        """






x = tf.ones((64, 28, 28, 1))
cm = CM_block(32, 3, input_shape=(28, 28, 1))
y = cm(x)
print(y)

