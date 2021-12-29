"""
https://www.tensorflow.org/guide/data

<tf.data API: Build tensorflow input pipelines>
The tf.data API introduces a tf.data.Dataset abstraction that represents a sequence of elements,
  in which each element consists of one or more components.
  For example, in an image pipeline, an element might be a single training example,
  with a pair of tensor components representing the image and its label.

tf.data.Dataset returns iterable object.

"""

import tensorflow as tf
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.set_printoptions(precision=4)
np_ds = pd.read_csv('data/Secom.csv')
x = np_ds.iloc[:,:-1]
y = np_ds.iloc[:,-1]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test))

print(train_dataset.element_spec)
x_, y_ = next(iter(train_dataset))

# example mnist fashion dataset - numpy dataset
from keras.api._v2 import keras
train_dataset, test_dataset = keras.datasets.fashion_mnist.load_data()
images_train, labels_train = train_dataset
images_test, labels_test = test_dataset

images_train = images_train/255
images_test = images_test/255
