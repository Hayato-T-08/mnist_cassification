import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np

model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128,activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(10,activation='softmax')
])
model.load_weights('mnist_weight.hdf5')

img=Image.open(f'temp.png').convert('L')
img_resize=img.resize((28,28))
img_array=np.array(img_resize)
imgs=img_array[np.newaxis,:,:]

pred = model.predict(imgs)

print(np.argmax(pred))