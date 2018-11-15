import numpy as np
import sys, os, re
from keras.preprocessing import image
from PIL import ImageOps
from PIL import Image

PATH = os.getcwd()

def loadDataset(dataset, loadAgain = False):
    if(loadAgain):
        dataPath = "%s/../dataSets/%s"%(PATH,dataset)
        characters = os.listdir(dataPath)
        characters = [char for char in characters if os.path.isdir("%s/%s"%(dataPath, char))]
        im = Image.open("%s/%s/%s"%(dataPath, characters[0], os.listdir("%s/%s"%(dataPath, characters[0]))[0] ))
        width, height = im.size
        del im
        X = np.zeros((1,height, width))
        Y = list()
        paths = list()
        counter = 0
        perc = 0
        for char in characters:
            images = os.listdir("%s/%s"%(dataPath,char))
            for im in images:
                counter += 1
                if(counter%800 == 0):
                    perc += 1
                    print(str(perc)+"%")
                imgPath = "%s/%s/%s"%(dataPath, char, im)
                paths.append(imgPath)
                Y.append(char)
                img = image.load_img(imgPath)
                img = img.convert('L')
                x = image.img_to_array(img)
                img.close()
                X = np.concatenate((X, x))
        X = np.delete(X, 0, axis=0)
        Y = np.asarray(Y)
        paths = np.asarray(paths)
        numpyPath = "%s/../numpyData/%s"%(PATH, dataset)
        XFile = open("%s/X.npy"%(numpyPath), 'bw')
        YFile = open("%s/Y.npy"%(numpyPath), 'bw')
        PathFile = open("%s/Path.npy"%(numpyPath), 'bw')
        np.save(XFile, X)
        np.save(YFile, Y)
        np.save(PathFile, paths)
        XFile.close()
        YFile.close()
        PathFile.close()
        return (X, Y, paths)
    else:
        numpyPath = "%s/../numpyData/%s"%(PATH, dataset)
        XFile = open("%s/X.npy"%numpyPath, 'br')
        YFile = open("%s/Y.npy"%numpyPath, 'br')
        PathFile = open("%s/Path.npy"%numpyPath, 'br')
        X = np.load(XFile)
        Y = np.load(YFile)
        paths = np.load(PathFile)
        XFile.close()
        YFile.close()
        PathFile.close()
        return (X,Y,paths)


# def loadHiraganaGit():
#     if("data" in os.listdir(PATH+"/../")):
#         XtrainFile = open(PATH+"/../data/Xtrain.npy", 'br')
#         YtrainFile = open(PATH+"/../data/Ytrain.npy", 'br')
#         x_train = np.load(XtrainFile)
#         y_train = np.load(YtrainFile)
#         XtrainFile.close()
#         YtrainFile.close()
#         return (x_train, y_train)
#     else:
#         data_path = PATH+'/../rawData/'
#         data = os.listdir(data_path)
#         x_train = np.zeros((1,84,83))
#         y_train = list()

#         for sample in data:
#             character = sample.rsplit(".",1)[0]
#             character = character.rsplit("kana",1)[1]
#             character = re.sub(r'\d+','',character)
#             img_path = data_path+sample
#             img = image.load_img(img_path)
#             img = img.convert('L')
#             x = image.img_to_array(img)
#             x_train = np.concatenate((x_train, x))
#             y_train.append(character)

#         x_train = np.delete(x_train, 0, 0)
#         y_train = np.array(y_train)

#         os.makedirs(PATH+"/../data")
#         XtrainFile = open(PATH+"/../data/Xtrain.npy", 'bw')
#         YtrainFile = open(PATH+"/../data/Ytrain.npy", 'bw')
#         np.save(XtrainFile, x_train)
#         np.save(YtrainFile, y_train)
#         XtrainFile.close()
#         YtrainFile.close()
#         return (x_train, y_train)