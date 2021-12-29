import tensorflow as tf

dataset_tmp = tf.data.Dataset.from_tensors([1,2,3])
dataset = tf.data.Dataset.from_tensor_slices([1,2,3])

for element in dataset:
    print(element)