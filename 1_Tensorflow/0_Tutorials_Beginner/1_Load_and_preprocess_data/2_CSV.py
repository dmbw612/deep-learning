import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
np.set_printoptions(precision=3, suppress=True)
import tensorflow as tf
from keras.api._v2 import keras
from keras import layers

secom = pd.read_csv('data/Secom.csv')
x = secom.copy()
y = x.pop('Y')

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,
                                                    shuffle=False, random_state=42)

model = keras.Sequential([
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])
model.compile(loss=keras.losses.BinaryCrossentropy(),
              optimizer=keras.optimizers.Adam(),
              metrics=keras.metrics.Recall())
model.fit(x_train, y_train, epochs=50)

y_pred = np.round(model.predict(x_test))
from sklearn.metrics import confusion_matrix
conf_mat = confusion_matrix(y_test, y_pred)
conf_mat = pd.DataFrame(conf_mat,
                        index=['True Negative', 'True Positive'],
                        columns=['Negative', 'Positive'])
recall = keras.metrics.Recall()(y_test, y_pred)