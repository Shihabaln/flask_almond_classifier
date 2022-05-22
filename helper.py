### Custom helper functions 

# Keras ML libraries
from keras.backend import set_session
import tensorflow as tf
from keras.models import load_model

# resize image 
import PIL.Image
import numpy as np
from skimage import transform

# Machine Learning Model Filename
Model_name = 'saved_model.h5'

def load_model_from_file():
    """ setting up the machine learning session by loading the model saved parameters
    :return: Model,session and graph
    """
    #Set up the machine learning session
    mySession = tf.compat.v1.Session()
    set_session(mySession)
    myModel = load_model(Model_name)
    myGraph = tf.compat.v1.get_default_graph()
    return (mySession,myModel,myGraph)

# Function to resize input to predection 
def load(filename):
    """ Function to resize unput image to fit requested size
    :param filename: image to be resized
    :return: image in numpy array format
    """
    np_image = PIL.Image.open(filename)
    np_image = np.array(np_image).astype('float32')/255
    np_image = transform.resize(np_image, (150, 150, 3))
    np_image = np.expand_dims(np_image, axis=0)
    return np_image