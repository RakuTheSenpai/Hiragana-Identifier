from loadData import loadDataset
from collections import Counter
import numpy as np 



def knn(x_train, y_train, x_test, y_test):
    correct = 0
    for testX, testY in zip(x_test, y_test):
        distances = list()
        for trainX, trainY in zip(x_train, y_train):
            distances.append( (trainY, np.linalg.norm(trainX-testX)) )
        distances = sorted(distances, key=lambda x: x[1])
        labels = list()
        for i in range(K):
            labels.append(distances[i][0])
        counter = Counter(labels)
        
        prediction = counter.most_common(1)[0][0]
        if(prediction == testY):
            correct += 1
    total = len(y_test)
    print("Accuracy = %s"%(correct/total))


K = 3  

X, Y, imgPaths = loadDataset("HiraganaGit", loadAgain = False)

indices = np.arange(len(X))
# np.random.seed(3)
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

knn(x_train, y_train, x_test, y_test)