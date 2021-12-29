"""
To differentiate automatically,
TensorFlow needs to remember what operations happen in what order during the forward pass.
Then, during the backward pass,
TensorFlow traverses this list of operations in reverse order to compute gradients
"""


import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

x = tf.Variable(3.0)
with tf.GradientTape() as tape:
    y = x**2

dy_dx = tape.gradient(target=y, sources=x)
print(dy_dx.numpy())

x = np.array([1, 2, 3], dtype=float).reshape(1, 3)
w = tf.Variable(tf.random.normal((3, 2)), name='w')
b = tf.Variable(tf.zeros((2,)), name='b')

with tf.GradientTape() as tape:
    y = x @ w + b
    loss = tf.reduce_sum(y**2)

[dl_dw, dl_db] = tape.gradient(loss, [w, b])
print(w.shape, dl_dw.shape)