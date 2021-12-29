import tensorflow_datasets as tfds

dataset_name = 'horses_or_humans'
batch_size = 32

dataset = tfds.load(dataset_name, split=tfds.Split.TRAIN)
dataset = dataset.shuffle(1024).batch(batch_size)

import tensorflow as tf

tf.nn.conv2d