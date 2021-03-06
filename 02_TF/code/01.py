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

# Let's see what the data actually looks like:
print(train_images[7])

# Use pyplot to see some of the images
plt.imshow(train_images[7], cmap=plt.cm.binary)
plt.show()