import tensorflow as tf
from tensorflow import keras
import numpy as np

data = keras.datasets.imdb

# Load the dataset
(train_data, train_labels), (test_data, test_labels) = data.load_data(num_words=10000)
# num_words=100000 reduces the data by filtering only the 100000 most common words
# this helps because if a word is to unfrequent it is difficult to analyze

# ---
# print(train_data[0])
    # [1, 14, 22, 16, 43, 530, 973, 1622, 1385, 65, 458, 4468, 66, 3941, 4, 173, 36, 256, 5, 25, 100, 43, 838, 112, 50, 670, 2, 9, 35, 480, 284, 5, 150, 4, 172, 112, 167, 2, 336, 385, 39, 4, 172, 4536, 1111, 17, 546, 38, 13, 447, 4, 192, 50, 16, 6, 147, 2025, 19, 14, 22, 4, 1920, 4613, 469, 4, 22, 71, 87, 12, 16, 43, 530, 38, 76, 15, 13, 1247, 4, 22, 17, 515, 17, 12, 16, 626, 18, 2, 5, 62, 386, 12, 8, 316, 8, 106, 5, 4, 2223, 5244, 16, 480, 66, 3785, 33, 4, 130, 12, 16, 38, 619, 5, 25, 124, 51, 36, 135, 48, 25, 1415, 33, 6, 22, 12, 215, 28, 77, 52, 5, 14, 407, 16, 82, 2, 8, 4, 107, 117, 5952, 15, 256, 4, 2, 7, 3766, 5, 723, 36, 71, 43, 530, 476, 26, 400, 317, 46, 7, 4, 2, 1029, 13, 104, 88, 4, 381, 15, 297, 98, 32, 2071, 56, 26, 141, 6, 194, 7486, 18, 4, 226, 22, 21, 134, 476, 26, 480, 5, 144, 30, 5535, 18, 51, 36, 28, 224, 92, 25, 104, 4, 226, 65, 16, 38, 1334, 88, 12, 16, 283, 5, 16, 4472, 113, 103, 32, 15, 16, 5345, 19, 178, 32]
# This list doesn't look like a movie review, but it is: each integer points to a word in a word list.
# ---

# keras already provides the word mapping in this case
word_index = keras.datasets.imdb.get_word_index()
# The original word_index has values starting at 1, but we will add new values
# So we need to offset the word_index to add this custom keys and values
word_index = {k:(v+3) for k,v in word_index.items()}
word_index['<PAD>'] = 0 # This will be used to make all reviews the same length (by adding padding, or zeros)
word_index['<START>'] = 1
word_index['<UNK>'] = 2
word_index['<UNUSED>'] = 3

# We need the reverse word mapping actually (we want to go: int -> str)
reverse_word_index = {v:k for k,v in word_index.items()}

# Function to decode the review
def decode_review(text):
    return " ".join([reverse_word_index.get(i, "?") for i in text])

# ---
# print(test_data[0])
# print(decode_review(test_data[0]))
# [1, 591, 202, 14, 31, 6, 717, 10, 10, 2, 2, 5, 4, 360, 7, 4, 177, 5760, 394, 354, 4, 123, 9, 1035, 1035, 1035, 10, 10, 13, 92, 124, 89, 488, 7944, 100, 28, 1668, 14, 31, 23, 27, 7479, 29, 220, 468, 8, 124, 14, 286, 170, 8, 157, 46, 5, 27, 239, 16, 179, 2, 38, 32, 25, 7944, 451, 202, 14, 6, 717]
# <START> please give this one a miss br br <UNK> <UNK> and the rest of the cast rendered terrible performances the show is flat flat flat br br i don't know how michael madison could have allowed this one on his plate he almost seemed to know this wasn't going to work out and his performance was quite <UNK> so all you madison fans give this a miss
# ---

# Now let's give all data the same length (remember that we will use one input neuron per value in each data item)
# Let's pick an arbitrary number (we could use the longest review but Tim's lazy)
# ---
# print(len(test_data[0]), len(test_data[1]))
# 68 260
# ---
items = [train_data, test_data]
for k in range(len(items)):
    items[k] = keras.preprocessing.sequence.pad_sequences(
        items[k],
        value=word_index['<PAD>'],
        padding="post",
        maxlen=250)
train_data, test_data = items
# ---
# print(len(test_data[0]), len(test_data[1]))
# 250 250
# ---

# Model
model = keras.Sequential()
model.add(keras.layers.Embedding(10000, 15))
model.add(keras.layers.GlobalAveragePooling1D())
model.add(keras.layers.Dense(16, activation="relu"))
model.add(keras.layers.Dense(1, activation="sigmoid"))