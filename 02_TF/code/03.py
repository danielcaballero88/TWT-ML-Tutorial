"""
First tutorial video from Tim:
Loading & Looking at Data
See README.md
"""
import tensorflow as tf
from tensorflow import keras
import numpy as np
from matplotlib import pyplot as plt

# Load keras dataset
data = keras.datasets.fashion_mnist

# Split the data to train/test subsets (Keras makes it very easy)
(train_images, train_labels), (test_images, test_labels) = data.load_data()

# Get the label names from the dataset (listed in the website)
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


# Normalize the data
train_images = train_images / 255.0
test_images = test_images / 255.0

# Create a model
model = keras.Sequential( # Sequential creates a sequence of layers
    [
        keras.layers.Flatten(input_shape=(28,28)), # first (input) layer is flatten
        keras.layers.Dense(128, activation="relu"), # middle layer, activation function="rectified linear unit" (negatives are made zero)
        keras.layers.Dense(10, activation="softmax") # final (output) layer, softmax makes all outputs add up to 1 (so, like probabilites)
    ]
)

# Set some parameters for our model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Train the model
model.fit(
    train_images,
    train_labels,
    epochs=10 # epochs state how many times the model is going to see tha train information
)

# Evaluate the model on the test data
test_loss, test_acc = model.evaluate(test_images, test_labels)
print("Tested Acc: ", test_acc)