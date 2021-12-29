import tensorflow as tf
from keras.api._v2 import keras
from keras.api._v2.keras.layers import Input, Dense, Conv2D, MaxPooling2D, AveragePooling2D, Flatten
from keras.api._v2.keras.models import Sequential, Model
from dmbw612.layers import CM_block, IdentityBlockConv


class CNNSequential(keras.models.Model):

    def __init__(self, input_shape, num_classes, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__input_shape = input_shape
        self.__num_classes = num_classes
        self.model = Sequential([
            Conv2D(32, 3, activation='relu', input_shape=self.__input_shape),
            MaxPooling2D(),

            Conv2D(64, 3, activation='relu'),
            MaxPooling2D(),

            Conv2D(128, 3, activation='relu'),
            MaxPooling2D(),

            Flatten(),
            Dense(256, activation='relu'),
            Dense(self.__num_classes)
        ])

    def call(self, inputs, training=None, mask=None):
        """
        (가정하건데) cnn.model이 실제 학습 네트워크임에도
        cnn = CNNSequential()
        cnn.compile, cnn.fit, cnn.evaluate가 모두 작동하는 것을 보면,
        어디선가 cnn = cnn.model이라고 알려줬다는 것인데,

        call 메서드를 지금과 같이 정의하기만 해도 위에 서술한 것이 작동하는 것을 보면,
        call에서 inputs을 받아 output을 내뱉는 CNNSequential.model이 self라고

        부모 클래스인 models.Model이 인식하는 듯 하다.
        따라서 models.Model을 상속해야지만
        compile, fit, evaluate 등의 메서드를 쉽게 수행할 수 있다.
        """
        return self.model(inputs)

    @property
    def input_shape(self):
        return self.__input_shape


class CNNModel(keras.models.Model):

    def __init__(self, input_shape, num_classes, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.shape = input_shape
        self.num_classes = num_classes

        self.inputs = Input(shape=self.shape)
        # callable(self.inputs()) #TypeError: 'KerasTensor' object is not callable
        self.conv_1 = Conv2D(32, 3, activation=tf.nn.relu)
        self.maxp_1 = MaxPooling2D()
        self.conv_2 = Conv2D(64, 3, activation=tf.nn.relu)
        self.maxp_2 = MaxPooling2D()
        self.conv_3 = Conv2D(128, 3, activation=tf.nn.relu)
        self.maxp_3 = MaxPooling2D()
        self.flatten = Flatten()
        self.fc = Dense(units=256, activation=tf.nn.relu)
        self.outputs = Dense(units=self.num_classes)

        x = self.conv_1(self.inputs)
        x1 = self.maxp_1(x)
        x = self.conv_2(x1)
        x2 = self.maxp_2(x)
        x = self.conv_3(x2)
        x3 = self.maxp_3(x)
        x = self.flatten(x3)
        x = self.fc(x)
        outputs = self.outputs(x)

        self.model = Model(self.inputs, outputs)
        # self.feature_map1 = Model(self.inputs, x1)
        # self.feature_map2 = Model(self.inputs, x2)
        # self.feature_map3 = Model(self.inputs, x3)

    def call(self, inputs, training=None, mask=None):
        return self.model(inputs)


class CNNModelBlock(keras.models.Model):

    def __init__(self, input_shape, num_classes):
        super().__init__()
        self.in_shape = input_shape
        self.num_classes = num_classes

        self.inputs = Input(shape=self.in_shape)
        self.cmblock_1 = CM_block(32, 3, input_shape=self.in_shape)
        self.cmblock_2 = CM_block(64, 3)
        self.cmblock_3 = CM_block(128, 3)
        self.flatten = Flatten()
        self.fc = Dense(units=256, activation=tf.nn.relu)
        self.outputs = Dense(units=self.num_classes)

        x = self.cmblock_1(self.inputs)
        x = self.cmblock_2(x)
        x = self.cmblock_3(x)
        x = self.flatten(x)
        x = self.fc(x)
        outputs = self.outputs(x)

        self.model = Model(inputs=self.inputs, outputs=outputs)

    def call(self, inputs, training=None, mask=None):
        return self.model(inputs)


class ResNet(keras.models.Model):

    def check_same_filters(self, i):
        if self.filters[i] == self.filters[i - 1]:
            return True
        else:
            return False

    def __init__(self, filters, kernel_size, input_shape, num_classes):
        super().__init__()
        self.filters = [filters[0]] + filters
        self.in_shape = input_shape
        self.num_classes = num_classes
        self._init_kernel_size = 7
        self._layers = {}

        for i in range(len(self.filters)):
            if i == 0:
                self.inputs = Input(shape=self.in_shape)
                self._layers[f'conv_{i}'] = Conv2D(filters=self.filters[i], kernel_size=self._init_kernel_size, strides=2, input_shape=self.in_shape)
                self.maxpool_1 = MaxPooling2D()
            else:
                is_same_filters = self.check_same_filters(i)
                self._layers[f'idblock_{i}'] = IdentityBlockConv(filters=self.filters[i], kernel_size=kernel_size, is_same_filters=is_same_filters)
        self.avgpool_2 = AveragePooling2D()
        self.flatten = Flatten()
        self.fc = Dense(self.num_classes)


        for i in range(len(filters)):
            if i == 0:
                x = self._layers[f'conv_{i}'](self.inputs)
                x = self.maxpool_1(x)
            else:
                x = self._layers[f'idblock_{i}'](x)
        x = self.avgpool_2(x)
        x = self.flatten(x)
        outputs = self.fc(x)

        self.model = Model(inputs=self.inputs, outputs=outputs)

    def call(self, inputs, training=None, mask=None):
        return self.model(inputs)
