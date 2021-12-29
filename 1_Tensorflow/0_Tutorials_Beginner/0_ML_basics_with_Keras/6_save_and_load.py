"""
callback 함수는 사용자가 사전에 정의해 놓은 특정 event가 발생할 때 자동으로 실행됩니다.
예를 들면 epoch이 끝나고 성능 향상이 없으면 학습을 멈춘다거나,
learning rate을 동적으로 조절하거나, 또는 학습 parameter를 저장한다 거나 할 수 있습니다.
callback 예시입니다.
callback = tf.keras.callbacks.EarlyStopping(monitor='loss', patience=3)
def scheduler(epoch):
    if epoch < 10:
        return 0.001
    else:
       return 0.001 * tf.math.exp(0.1 * (10 - epoch))
callback = tf.keras.callbacks.LearningRateScheduler(scheduler)
# lr = self.schedule(epoch)
# K.set_value(self.model.optimizer.lr, K.get_value(lr))
model.fit(dataset, epochs=100, callbacks=[callback])
"""


import os
import numpy as np
import tensorflow as tf
from keras.api._v2 import keras
from pathlib import Path
np.set_printoptions(precision=3)
print(tf.__version__)


train_ds, test_ds = keras.datasets.mnist.load_data()
train_images, train_label = train_ds
test_images, test_label = test_ds
train_images, train_label = train_images[:1000].reshape(-1,28*28), train_label[:1000]
test_images, test_label = test_images[:1000].reshape(-1,28*28), test_label[:1000]


def create_model():
    model=keras.models.Sequential([
        keras.layers.Dense(512, activation='relu', input_shape=(784,)),
        keras.layers.Dropout(0.2),
        keras.layers.Dense(10)
    ])

    model.compile(loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  optimizer=keras.optimizers.Adam(),
                  metrics=[keras.metrics.SparseCategoricalAccuracy()])
    return model


# # (1) just one ckpt
# ckpt_filepath = Path(__file__).parent.resolve().joinpath('training_1/cp.ckpt')
# ckpt_dir = ckpt_filepath.parent.resolve()
# cp_callback = keras.callbacks.ModelCheckpoint(filepath=ckpt_filepath,
#                                               save_weights_only=True,
#                                               verbose=1)
# model = create_model()
# model.fit(x=train_images,
#           y=train_label,
#           epochs=10,
#           validation_data=0.1,
#           callbacks=[cp_callback])
# os.listdir(ckpt_dir)
# model.load_weights(filepath=ckpt_filepath)
# loss, acc = model.evaluate(test_images, test_label, verbose=2)
# print("Restored model, accuracy: {:5.2f}%".format(100 * acc))

# (2) save and load with ckpt
# (2-1) to make ckpt_callback
# ckpt_filepath = Path(__file__).parent.resolve().joinpath('training_2/cp-{epoch:04d}.ckpt')
# print(ckpt_filepath)
# ckpt_dir = ckpt_filepath.parent.resolve()
# batch_size = 32
# ckpt_callback = keras.callbacks.ModelCheckpoint(
#     filepath=ckpt_filepath,
#     verbose=1,
#     save_weights_only=True,
#     save_freq=5*batch_size
# )
#
#
# (2-2) save ckpt regularly
# model = create_model()
# model.save_weights(filepath=ckpt_filepath.__str__().format(epoch=0))
# model.fit(x=train_images,
#           y=train_label,
#           epochs=50,
#           batch_size=batch_size,
#           callbacks=[ckpt_callback],
#           validation_split=0.1,
#           verbose=0)
#
# (2-3) load weights by ckpt and evaluate
# latest_path = tf.train.latest_checkpoint(checkpoint_dir=ckpt_dir)
# print(latest_path)
# model = create_model()
# model.load_weights(filepath=latest_path)
# loss, acc = model.evaluate(x=test_images,
#                            y=test_label,
#                            verbose=2)


# (3) save and load model using SavedModel format
SAVED_MODEL_DIR = 'saved_model/'
saved_model_filename = 'my_model'

model = create_model()
model.fit(x=train_images,
          y=train_label,
          epochs=5)
os.makedirs(SAVED_MODEL_DIR, exist_ok=True)
model.save(filepath=SAVED_MODEL_DIR+saved_model_filename)

model = create_model()
model = keras.models.load_model(SAVED_MODEL_DIR+saved_model_filename)
loss, acc = model.evaluate(x=test_images,
                           y=test_label,
                           verbose=2)
print("Restored model, accuracy: {}".format(100*acc))