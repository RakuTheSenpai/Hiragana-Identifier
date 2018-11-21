import pickle as pkl 
import matplotlib.pyplot as plt
import os

PATH = os.getcwd()

historyFile = open(PATH+"/../models/history.pkl", 'rb')
history = pkl.load(historyFile)
historyFile.close()

epochs = range(1,len(history['acc'])+1)

plt.ylabel("Accuracy")
plt.xlabel("Epochs/Iterations")
plt.plot(epochs, history['acc'], label="Training")
plt.plot(epochs, history['val_acc'], label="Testing")
plt.legend()
plt.show()