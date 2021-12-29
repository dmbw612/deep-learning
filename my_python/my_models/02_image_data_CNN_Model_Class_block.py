from pathlib import Path
import numpy as np
import PIL.Image
import tensorflow as tf
from keras.api._v2 import keras
from dmbw612.models import CNNModelBlock

print(f'tf.version {tf.__version__}')
print(f'keras.version {keras.__version__}\n')

# checkpoint callbacks
filename = Path(__file__).stem
parent_dir = Path(__file__).parent.parent.resolve()  # my_python
saved_model_dir = parent_dir.joinpath(f'saved_models/{filename}')
ckpt_filepath = saved_model_dir.joinpath('cp-{epoch:04d}.ckpt')
ckpt_dir = ckpt_filepath.parent.parent.resolve()  # image_data_training
ckpt_callback = keras.callbacks.ModelCheckpoint(
    filepath=ckpt_filepath,
    save_weights_only=True,
    save_freq='epoch',
    verbose=0,
)

# image data from directory
dataset_url = "https://storage.googleapis.com/download.tensorflow.org/example_images/flower_photos.tgz"
data_dir = keras.utils.get_file(origin=dataset_url, fname='flower_photos', untar=True)  # Download a file
data_dir = Path(data_dir)
image_count = len(list(data_dir.glob('*/*.jpg')))
roses_path = list(data_dir.glob('roses/*'))
img = PIL.Image.open(roses_path[1].__str__())
print('the number of total flower images: ', image_count)
print('image size of a rose sample: ', np.array(img).shape)

batch_size = 32
img_height = 180
img_width = 180

print('image_dataset_from_directory generates one-hot encoding labels.')
train_ds = keras.utils.image_dataset_from_directory(
    data_dir,
    label_mode='categorical',
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(img_height, img_width),
)

test_ds = keras.utils.image_dataset_from_directory(
    data_dir,
    label_mode='categorical',
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(img_height, img_width),
)

for images_batch, labels_batch in train_ds:
    print('image batch size: ', images_batch.shape)
    print('label batch size: ', labels_batch.shape)
    print('label sample: ', labels_batch[0])
    print('REMEMBER!! Labels is encoded in one=hot encoding.\n')
    break
num_classes = len(train_ds.class_names)
input_shape = (img_height, img_width, 3)
print('We got inputs of create_model function: input_shape, num_classes\n')

normalization_layer = keras.layers.Rescaling(1. / 255)
train_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
test_ds = test_ds.map(lambda x, y: (normalization_layer(x), y))


if __name__ == '__main__':

    training = False

    cnn = CNNModelBlock(input_shape=input_shape, num_classes=num_classes)
    cnn.compile(
        loss=keras.losses.CategoricalCrossentropy(from_logits=True),
        optimizer=keras.optimizers.Adam(),
        metrics=[keras.metrics.CategoricalAccuracy()]
    )

    if training:
        cnn.save_weights(filepath=ckpt_filepath.__str__().format(epoch=0))
        history = cnn.fit(train_ds,
                            epochs=3,
                            callbacks=[ckpt_callback],
                            validation_data=test_ds
                            )
    else:
        ckpt_dir = ckpt_filepath.parent.resolve()
        latest_path = tf.train.latest_checkpoint(checkpoint_dir=ckpt_dir)
        print('latest_filepath: ', latest_path)

        cnn.load_weights(filepath=latest_path)
        cnn.summary()
        loss, acc = cnn.evaluate(test_ds)
        print("Restored CNN, accuracy: {}".format(100 * acc))
