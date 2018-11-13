import numpy as np
import sys, os, re
from keras.preprocessing import image
from PIL import ImageOps


def loadHiragana2():
    PATH = os.getcwd()
    if("data" in os.listdir(PATH+"/../")):
        XtrainFile = open(PATH+"/../data/Xtrain.npy", 'br')
        YtrainFile = open(PATH+"/../data/Ytrain.npy", 'br')
        x_train = np.load(XtrainFile)
        y_train = np.load(YtrainFile)
        XtrainFile.close()
        YtrainFile.close()
        return (x_train, y_train)
    else:
        data_path = PATH+'/../rawData/'
        data = os.listdir(data_path)
        x_train = np.zeros((1,84,83))
        y_train = list()

        for sample in data:
            character = sample.rsplit(".",1)[0]
            character = character.rsplit("kana",1)[1]
            character = re.sub(r'\d+','',character)
            img_path = data_path+sample
            img = image.load_img(img_path)
            img = img.convert('L')
            x = image.img_to_array(img)
            x_train = np.concatenate((x_train, x))
            y_train.append(character)

        x_train = np.delete(x_train, 0, 0)
        y_train = np.array(y_train)

        os.makedirs(PATH+"/../data")
        XtrainFile = open(PATH+"/../data/Xtrain.npy", 'bw')
        YtrainFile = open(PATH+"/../data/Ytrain.npy", 'bw')
        np.save(XtrainFile, x_train)
        np.save(YtrainFile, y_train)
        XtrainFile.close()
        YtrainFile.close()
        return (x_train, y_train)
