"""
https://keras.io/guides/functional_api/
이곳은 bible과 같은 곳... 여기서 기초를 닦으면 될듯
"""

import tensorflow as tf
print(tf)
# <module 'tensorflow' from 'C:\\Users\\B612\\anaconda3\\envs\\dmbw612\\lib\\site-packages\\tensorflow\\__init__.py'>


from tensorflow import keras
print(keras)
# <module 'keras.api._v2.keras' from 'C:\\Users\\B612\\anaconda3\\envs\\dmbw612\\lib\\site-packages\\keras\\api\\_v2\\keras\\__init__.py'>
# ISSUE1. keras의 위치. from tensorflow 했는데 다른 곳에서 keras를 불러오네. 자동적으로 이루어지는 일들임.


""" 
the functional API is a way to build <graphs of layers> 
"""

from tensorflow.keras import layers
inputs = layers.Input(shape=(784,)) # layers.Input function returns a `tensor`.
# input_layer.py의 Input function 위에 보면
# @keras_export('keras.layers.Input', 'keras.Input') # @keras_export 데코레이터는 아래와 같이 정의되는데,
# keras_export = functools.partial(api_export, api_name=KERAS_API_NAME)# functools.partila을 사용한다. 이것은 객체를 받아 api_name인자가 채워진 새로운 객체로 반환한다. 그럼 api_export 객체가 중요하겠지요.
# class api_export(object):  # 얘도 클래스네. 그러니까 keras_export는 api_export랑 api_name이 입력되었을 뿐 다를바 없네.

#
# @keras_export('keras.layers.Input', 'keras.Input')
# def Input(...):
#   input_layer = InputLayer(**input_layer_config)
#   outputs = input_layer._inbound_nodes[0].output_tensors
#   if len(outputs) == 1:
#     return outputs[0]
#   else:
#     return outputs
from tensorflow.keras.layers import InputLayer
# inputs_layer = layers.InputLayer(input_shape=(28*28,)) # layers.InputLayer CLASS craetes an 'object'
# inputs = inputs_layer.output # object's output tensor
print(layers.Input)
print(inputs)

""" You create a new node (dense layer) in the graph of layers by <calling a layer on this inputs object> """
dense = layers.Dense(64, activation='relu') # layers.Dense Class returns a 'object'.
print(layers.Dense)
print(dense)
print("Is dense layer callable? %s"%callable(dense))
x = dense(inputs) # dense layer object가 call 함수를 통해 inputs object를 호출한다.

x = layers.Dense(64, activation='relu')(x)
outputs = layers.Dense(10)(x)

model = keras.Model(inputs=inputs, outputs=outputs, name="mnist_model")
model.summary()
keras.utils.plot_model(model, "my_first_model.png", show_shapes=True)

model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=keras.optimizers.RMSprop(),
    metrics=["accuracy"],
)

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train.reshape(60000, 784).astype("float32") / 255
x_test = x_test.reshape(10000, 784).astype("float32") / 255
history = model.fit(x_train, y_train, batch_size=64, epochs=2, validation_split=0.2)

test_scores = model.evaluate(x_test, y_test, verbose=2)
print("Test loss:", test_scores[0])
print("Test accuracy:", test_scores[1])

from tensorflow.keras import layers
import tensorflow as tf
l = layers.Dense(10)



