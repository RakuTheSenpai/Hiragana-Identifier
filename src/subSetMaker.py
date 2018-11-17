import numpy as np
import random 
#Function divides into subset for cross validation
def subSetMaker(x_train,y_train,k):
    size = x_train.size
    indexes = np.arange(size)
    random.shuffle(indexes)
    x_train = x_train[indexes]
    y_train = y_train[indexes]
    x_result = list()
    y_result = list()
    lowerbound = 0
    for i in range(1,k + 1):
        upperbound = (int) (i * size / k)
        x_result.append(x_train[lowerbound:upperbound])
        y_result.append(y_train[lowerbound:upperbound])
        lowerbound = upperbound
    return (x_result,y_result)
