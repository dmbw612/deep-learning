import numpy as np
import os
import PIL
import PIL.Image
import tensorflow as tf
from keras.api._v2 import keras
import tensorflow_datasets as tfds


print(tf.__version__)
print(keras.__version__)


import pathlib # path를 객체화. 객체로 다루면 좋은 점은 연산자를 새롭게 정의할 수 있음.
dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
data_dir = keras.utils.get_file(origin=dataset_url, fname='flower_photos', untar=True)
# data_dir = 'C:\\Users\\B612\\.keras\\datasets\\flower_photos'
data_dir = pathlib.Path(data_dir)
image_count = len(list(data_dir.glob('*/*.jpg')))
print(image_count)
roses = list(data_dir.glob('roses/*'))
img = PIL.Image.open(roses[1].__str__())
# img.show()


batch_size = 32
img_height = 180
img_width = 180


train_ds = keras.utils.image_dataset_from_directory(
    data_dir,
    label_mode='categorical',
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size
)


test_ds = keras.utils.image_dataset_from_directory(
    data_dir,
    label_mode='categorical',
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(img_height, img_width),
    batch_size=batch_size
)
class_names = train_ds.class_names
num_classes = len(class_names)
print(class_names)


for images_batch, labels_batch in train_ds:
    print(images_batch.shape)
    print(labels_batch.shape)
    break
# layers에 있는 class는 tensor를 입력으로 받아 tensor를 return하는 class임을 잊지말자.
normalization_layer = keras.layers.Rescaling(1./255)
normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
images_batch, labels_batch = next(iter(normalized_ds))
# iter(a)은 iterator가 아닌 a를 iterator로 바꿔준다.
# next는 iterator의 아이템을 호출한다.
print(np.min(images_batch), np.max(images_batch))


model = keras.Sequential([
    keras.layers.Rescaling(1./255),
    keras.layers.Conv2D(32, 3, activation='relu'),
    keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(32, 3, activation='relu'),
    keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(32, 3, activation='relu'),
    keras.layers.MaxPooling2D(),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(num_classes)
])
model.compile(loss=keras.losses.CategoricalCrossentropy(from_logits=True),
              optimizer=keras.optimizers.Adam(),
              metrics=keras.metrics.Accuracy()
              )
# Adam은 어떻게 작동되는 것일까? -> 정의에 가서 usage살펴보세요.
# Logits은 log(p/(1-p))으로 정의되어, p가 0부터 1까지 변할 때, -무한~무한까지 변합니다.
# 따라서 softmax를 취한 layer가 model에 있으면 default인 from_logits=False를 그래도 사용합니다.


model.fit(train_ds, validation_data=test_ds, epochs=3)
# train_ds에는 1 epoch에 사용되는 온전한 data가 들어가 있다.
""" 이 아래는 빠르게 접근 가능하고 잘 섞어서 batch로 데이터 내주는 코드입니다. 나중에 사용해 보세요."""
# def configure_for_performance(ds):
#   ds = ds.cache()
#   ds = ds.shuffle(buffer_size=1000)
#   ds = ds.batch(batch_size)
#   ds = ds.prefetch(buffer_size=tf.data.AUTOTUNE)
#   return ds
#
# train_ds = configure_for_performance(train_ds)
# val_ds = configure_for_performance(val_ds)