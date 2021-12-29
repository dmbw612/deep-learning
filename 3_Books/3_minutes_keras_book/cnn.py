from sklearn import model_selection, metrics
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import matplotlib.pyplot as plt
import os

import tensorflow as tf
from tensorflow import keras

import tensorflow.keras.backend as K
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Dropout

class CNN(Model):
    def __init__(self,  nb_classes, in_shape=None):
        self.nb_classes = nb_classes
        self.in_shape = in_shape
        self.build_model()
        super().__init__(self.x, self.y)
        self.compile()

    def build_model(self):
        nb_classes = self.nb_classes
        in_shape = self.in_shape

        x = Input(in_shape)
        h = Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=in_shape)(x)
        h = Conv2D(64, kernel_size=(3,3), activation='relu')(h)
        h = MaxPooling2D(pool_size=(2,2))(h)
        h = Dropout(0.25)(h)
        h = Flatten()(h)

        cl_part = Model(x, h)

        h = Dense(128, activation='relu')(h)
        h = Dropout(0.5)(h)

        fl_part = Model(x, h)

        y = Dense(nb_classes, activation='sotfmax', name='preds')(h)

        self.cl_part = cl_part
        self.fl_part = fl_part
        self.x = x
        self.y = y

    def compile(self):
        Model.compile(self, loss='categorical_crossentropy',
                      optimizer='adadelta', metrics=['accuracy'])

# class DataSet:
#     def __init__(self, X, y, nb_classes, scaling=True, test_size=0.2, random_state=0):

