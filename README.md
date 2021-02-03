# Tec With Tim - Machine Learning - Tutorial

I'll follow [Tec With Tim's tutorial on Machine Learning][1].

It is an introductory tutorial on Machine Learning, previous to Deep Learning
and Neural Networks.

The tutorial also has a [text version][2] in Tim's website.

The data used is from the popular [UCI Machine Learning Repository][3].

[1]: https://youtube.com/playlist?list=PLzMcBGfZo4-mP7qA9cagf68V06sko5otr
[2]: https://www.techwithtim.net/tutorials/machine-learning-python/linear-regression/
[3]: https://archive.ics.uci.edu/ml/index.php
# 1. Introduction

1. Set up virtual environment.
2. Installation of tensorflow and keras.
3. Import.

# 2. Linear Regression

See file: `code/01.ipynb`

# 3. Saving Models and Plotting Data

See file: `code/01.ipynb` (search for the title)

# 4. KNN: K-nearest Neighbor

See file: `code/02.ipynb` (search for the title)

In this case we work with ***irregular data***, meaning that the dataset was
not previously prepared for as in a nice csv file with no missing values and no
wrong values.

KNN searches for the <k> nearest neighbors.
To do that it needs to compute the distance for **all** points, and then it
only keeps the k nearest.
As a result it is very slow when calculating predictions and it doesn't quite
make sanse to save the model, as it was the case of Linear Regression.

Nice explanation and pictures at [Tim's Website][4]

[4]: https://www.techwithtim.net/tutorials/machine-learning-python/k-nearest-neighbors-3/

