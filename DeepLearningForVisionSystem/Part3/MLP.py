import tensorflow as tf
print("Tensorflow version is ", tf.__version__)
from tensorflow import keras

import numpy as np 
import matplotlib.pyplot as plt

from keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_train.shape)


# Data show
plt.figure()
plt.imshow(x_train[0]) # train_image.shape = (781,)
plt.colorbar()
plt.grid(False)
plt.show()

# data normalize
x_train = x_train/255.0
x_test = x_test/255.0

# Model make
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(512, activation="relu"),
    keras.layers.Dense(512, activation="relu"),
    keras.layers.Dense(10, activation="softmax")
])

# Model compile
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10)
