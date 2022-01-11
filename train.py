from keras.preprocessing.image import ImageDataGenerator

from keras.models import Sequential
from keras.layers import Conv2D, Activation, MaxPooling2D, Flatten, Dense, Dropout
import tensorflow as tf
from tensorflow.keras import backend as K

#Set the image size with are learning from
Img_width, Img_height = 150,150

#Set the constants
Train_data = 'train'
Validation_data = 'validation'
No_train = 20   #Must match number of files
No_validation = 20

Epochs = 50 
Batch = 5

# Machine Learning Model Filename
Model_name = 'saved_model.h5'

def build_model():
    
    if K.image_data_format() == 'channels_first':
        input_shape = (3, Img_width, Img_height)
    else:
        input_shape = (Img_width, Img_height, 3)

    model = Sequential()
    model.add(Conv2D(32, (3, 3), input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1))
    model.add(Activation('sigmoid'))
    
    model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

    return model


def train_model(model):
    # this is the augmentation configuration we will use for training
    train_datagen = ImageDataGenerator(
            rotation_range = 40,
            width_shift_range = 0.2,
            height_shift_range = 0.2,
            rescale = 1.0/255,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            fill_mode='nearest')
    
    
    # only rescaling
    test_datagen = ImageDataGenerator(rescale= 1. / 255)

    train_generator = train_datagen.flow_from_directory(
            Train_data,
            target_size=(Img_width, Img_height),
            batch_size=Batch,
            class_mode='binary')

    validation_generator = test_datagen.flow_from_directory(
            Validation_data,
            target_size=(Img_width, Img_height),
            batch_size=Batch,
            class_mode='binary')
    
    model.fit_generator(
            train_generator,
            steps_per_epoch=No_validation // Batch,
            epochs=Epochs,
            validation_data=validation_generator,
            validation_steps=No_validation // Batch)
     
    return model



def main():
    myModel = None
    tf.keras.backend.clear_session()
    myModel = build_model()
    myModel = train_model(myModel)
    myModel.save(Model_name)


main()
