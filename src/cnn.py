import numpy as np
from loadData import loadDataset
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils

#DON'T TOUCH, I DON'T KNOW WHAT IT DOES##
from keras import backend as K         ##
K.set_image_dim_ordering('th')         ##
#########################################

import matplotlib.pyplot as plt

from subSetMaker import subSetMaker

def plots(x, y, title, xlabel, ylabel, color = 'r'):
	y = y.reshape((len(x),))
	plt.plot(x,y, color=color)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(title)
	plt.show()

def baseline_model():
	# create model
	model = Sequential()
	model.add(Conv2D(50, (5, 5), input_shape=(1, 84, 83), data_format='channels_first', activation='relu'))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Flatten())
	model.add(Dense(128, activation='relu'))
	model.add(Dense(num_classes, activation='softmax'))
	# Compile model
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model


DATASET = "Hiragana73"
# DATASET = "HiraganaGit"

#SWITCH THE LINES BELOW IF YOU NEED TO LOAD ALL THE DATA FROM THE DATASET AGAIN
X, Y, imgPaths = loadDataset(DATASET, loadAgain=True)
# X, Y, imgPaths = loadDataset(DATASET, loadAgain=False)

X /= 255

#X has format (height, width, N)

indices = np.arange(X.shape[0])
np.random.seed(3)
np.random.shuffle(indices)
X = X[indices]
Y = Y[indices]

N = X.shape[0]

Ntrain = int(N*80/100)
Ntest = int(N*20/100)

x_train = X[:Ntrain].reshape((Ntrain, 1, 84, 83))
y_train = Y[:Ntrain]

x_test = X[Ntrain:Ntrain+Ntest].reshape((Ntest, 1, 84, 83))
y_test = Y[Ntrain:Ntrain+Ntest]

#CONVERT CLASSES TO NUMBERS

labelToNumber = dict()
numberToLabel = dict()
counter = 0
for i in range(len(y_train)):
    if(y_train[i] not in labelToNumber):
        labelToNumber[y_train[i]] = counter
        counter += 1
    y_train[i] = labelToNumber[y_train[i]]

for i in range(len(y_test)):
    if(y_test[i] not in labelToNumber):
        labelToNumber[y_test[i]] = counter
        counter += 1
    y_test[i] = labelToNumber[y_test[i]]

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

#NUMBER OF CLASSES
num_classes = y_train.shape[1]
num_epochs = 10
epochs = range(1,num_epochs+1)

model = baseline_model()
metrics = model.fit(x_train, y_train, validation_data = (x_test, y_test), epochs=num_epochs, batch_size=10) #returns val_loss, val_acc, loss, acc
# train_error = metrics.history['acc']

# train_error = np.ones(epochs)-train_error
# plots(epochs, train_error, "Error de entrenamiento", "Epoch", "Error")


# scores = model.evaluate(x_test, y_test)
# print("CNN Error: %.2f%%" % (100-scores[1]*100))