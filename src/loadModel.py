from keras.models import model_from_json
import pickle as pkl
import os

PATH = os.getcwd()


def loadModel():
    json_file = open(PATH+'/../models/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(PATH+"/../models/model.h5")
    print("Loaded model from disk")
    loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return loaded_model