import numpy as np
from loadData import loadDataset
from loadModel import loadModel
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
from frontend import createGUI
import os
import pickle as pkl

#DON'T TOUCH, I DON'T KNOW WHAT IT DOES##
from keras import backend as K         ##
K.set_image_dim_ordering('th')         ##
#########################################

import matplotlib.pyplot as plt

from subSetMaker import subSetMaker

PATH = os.getcwd()

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


# DATASET = "Hiragana73"
DATASET = "HiraganaGit"

#SWITCH THE LINES BELOW IF YOU NEED TO LOAD ALL THE DATA FROM THE DATASET AGAIN
X, Y, imgPaths = loadDataset(DATASET, loadAgain=True)
#X, Y, imgPaths = loadDataset(DATASET, loadAgain=False)

X /= 255

#X has format (height, width, N)

indices = np.arange(X.shape[0])
np.random.seed(3)
np.random.shuffle(indices)
X = X[indices]
Y = Y[indices]
imgPaths = imgPaths[indices]

N = X.shape[0]

TRAIN_RATIO = 80

Ntrain = int(N*TRAIN_RATIO/100)
Ntest = int(N*(100-TRAIN_RATIO)/100)

x_train = X[:Ntrain].reshape((Ntrain, 1, 84, 83))
y_train = Y[:Ntrain]
paths_train = imgPaths[:Ntrain]

x_test = X[Ntrain:Ntrain+Ntest].reshape((Ntest, 1, 84, 83))
y_test = Y[Ntrain:Ntrain+Ntest]
paths_test = imgPaths[Ntrain:Ntrain+Ntest]
orig_y_test = np.copy(y_test)

#CONVERT CLASSES TO NUMBERS

labelToNumber = dict()
numberToLabel = dict()
counter = 0
for i in range(len(y_train)):
    if(y_train[i] not in labelToNumber):
        labelToNumber[y_train[i]] = counter
        numberToLabel[counter] = y_train[i]
        counter += 1
    y_train[i] = labelToNumber[y_train[i]]

for i in range(len(y_test)):
    if(y_test[i] not in labelToNumber):
        labelToNumber[y_test[i]] = counter
        numberToLabel[counter]=y_test[i]
        counter += 1
    y_test[i] = labelToNumber[y_test[i]]

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

#NUMBER OF CLASSES
num_classes = y_train.shape[1]
num_epochs = 5

trainAgain = False
if trainAgain:
    model = baseline_model()
    metrics = model.fit(x_train, y_train, validation_data = (x_test, y_test), epochs=num_epochs, batch_size=10) #returns val_loss, val_acc, loss, acc
    modelJSON = model.to_json()
    # serialize model to JSON
    model_json = model.to_json()
    with open(PATH+"/../models/model.json", "w") as json_file:
        json_file.write(model_json)
    #serialize training history
    with open(PATH+"/../models/history.pkl", 'wb') as file_pi:
        pkl.dump(metrics.history, file_pi)
    # serialize weights to HDF5
    model.save_weights(PATH+"/../models/model.h5")
    print("Saved model to disk")
else:
    model = loadModel()
    y_pred = model.predict_classes(x_test)
    y_pred = [numberToLabel[char] for char in y_pred]
    createGUI(orig_y_test, y_pred, paths_test)