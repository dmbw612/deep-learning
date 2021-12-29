import numpy as np
import tensorflow as tf
from keras.api._v2 import keras


class CustomModel(keras.models.Model):

    def train_step(self, data):
        """
        This method should contain the mathematical logic for one step of training.
        This typically includes the forward pass, loss calculation, backpropagation,
        and metric updates.

        Returns:
          A `dict` containing values that will be passed to
          `tf.keras.callbacks.CallbackList.on_train_batch_end`. Typically, the
          values of the `Model`'s metrics are returned. Example:
          `{'loss': 0.2, 'accuracy': 0.7}`.


        데이터를 받아서 forward를 진행하여 loss를 계산하고,
        계산된 loss에 대해 변수별로 gradient 값을 구합니다.
        그리고 변수 값을 구해진 gradient를 통해 업데이트 해줍니다.
        """
        x, y = data

        with tf.GradientTape() as tape:
            y_pred = self(x, training=True)
            loss = self.compiled_loss(y, y_pred, regularization_losses=self.losses)

        # Compute gradients
        trainable_vars = self.trainable_variables
        gradients = tape.gradient(loss, trainable_vars)

        # Update weights
        # grads_and_vars = tf.gradients(loss, var) 이건 어떤 경우에 쓰나 생각해보기.
        self.optimizer.apply_gradients(zip(gradients, trainable_vars))

        # Update metrics
        self.compiled_metrics.update_state(y, y_pred)
        """
        `MeanMetricWrapper.result()` will return the average metric value across all samples seen so far.
        """
        return {m.name: m.result() for m in self.metrics}


# Construct and compile an instance of CustomModel
inputs = keras.Input(shape=(32,))
outputs = keras.layers.Dense(1)(inputs)
model = CustomModel(inputs, outputs)
model.compile(optimizer="adam", loss="mse", metrics=["mae"])

# Just use `fit` as usual
x = np.random.random((1000, 32))
x_t = np.random.random((500, 32))
y = np.random.random((1000, 1))
y_t = np.random.random((500, 1))
model.fit(x, y, epochs=10, validation_data=(x_t, y_t))


loss_tracker = keras.metrics.Mean(name='loss')
mae_metric = keras.metrics.MeanAbsoluteError(name='mae')


class CustomModelLowLevel(keras.Model):
    def train_step(self, data):
        x, y = data

        with tf.GradientTape() as tape:
            y_pred = self(x, training=True)
            loss = keras.losses.mean_squared_error(y, y_pred)

        trainable_vars = self.trainable_variables
        gradients = tape.gradient(loss, trainable_vars)

        self.optimizer.apply_gradients(zip(gradients, trainable_vars))

        loss_tracker.update_state(loss)
        mae_metric.update_state(y, y_pred)
        return {
            "loss": loss_tracker.result(),
            "mae": mae_metric.result()
        }

    @property
    def metrics(self):
        # We list our `Metric` objects here so that `reset_states()` can be
        # called automatically at the start of each epoch
        # or at the start of `evaluate()`.
        # If you don't implement this property, you have to call
        # `reset_states()` yourself at the time of your choosing.
        return [loss_tracker, mae_metric]

x = np.random.random((1000, 32))
y = np.random.random((1000,1))

inputs = keras.layers.Input((32,))
outputs = keras.layers.Dense(1)(inputs)
model = CustomModelLowLevel(inputs, outputs)
model.compile(optimizer='adam')
model.fit(x, y, epochs=5)