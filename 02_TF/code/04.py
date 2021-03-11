"""
First tutorial video from Tim:
Loading & Looking at Data
See README.md
"""
import tensorflow as tf
from tensorflow import keras
import numpy as np
from matplotlib import pyplot as plt
import os

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

# Load the already saved model
here = os.path.dirname(__file__)
modelfile = os.path.join(here, "03_keras_model")
model = keras.models.load_model(modelfile)

# To predict use the method 'predict'
prediction = model.predict(test_images) # The output is a list of lists, where each list has the values for the output neurons
# print(prediction)
# out:
# [[4.4958400e-05 6.6604180e-06 2.2885768e-05 ... 1.1098782e-01
#   1.1161214e-03 8.3919060e-01]
#  [1.0093011e-04 2.2287279e-05 9.8917657e-01 ... 4.8820544e-12
#   4.6799281e-07 1.4377058e-09]
#  [3.4428311e-05 9.9993038e-01 9.4786674e-07 ... 2.2779127e-09
#   6.8554883e-08 5.6520733e-11]
#  ...
#  [6.2878788e-02 2.8639184e-05 1.6297556e-03 ... 4.7323836e-05
#   8.5094982e-01 2.3462737e-06]
#  [2.8881307e-06 9.9948406e-01 5.1311525e-07 ... 8.2216431e-08
#   8.9881773e-08 2.4221361e-08]
#  [1.0151759e-03 8.4442909e-05 1.4469009e-03 ... 6.3388444e-02
#   6.2348531e-03 6.5696379e-03]]

for _ in range(5):
    k = np.random.randint(len(prediction))
    plt.grid(False)
    plt.imshow(test_images[k], cmap=plt.cm.binary)
    plt.xlabel("Actual: " + class_names[test_labels[k]])
    plt.title("Prediction: " + class_names[np.argmax(prediction[k])] + " with value " + str(np.max(prediction[k])))
    plt.show()