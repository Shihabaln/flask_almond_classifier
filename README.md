# Almond Classifier 
This project motivation is to utilize neural networks in evaluating almonds categories. Two categories were used in this project, normal and broken almonds . 


# Technologies
* Flask
* Tensorflow ==2.7.0
* Pillow 
* SciPy
* Scikit-image = 0.19.0

# Model
The neural networks model architecture called “convolutional” networks short for “CNN” which works best with images. CNN works well with images as they look for pattern at the pixel level then proceed to gather more information for larger areas and more groups of pixels to extract more complex features from images. The trained model will then be used as a backend for the almond classifier app that will predict the weight of the uploaded image and attempt to classify its category. 
![modelsummary](https://user-images.githubusercontent.com/83282165/170724089-55096080-07f0-43ff-8b6c-7d720764eb18.jpg)



The project report can be found [here](report.pdf).

# Demo 
Classify into nomral or broken almonds
 flask

![Screenshot 2022-05-19 135100](https://user-images.githubusercontent.com/83282165/169712618-29bc7cec-c60a-4568-9589-d0769aed989f.jpg)

![Screenshot 2022-01-11 115102](https://user-images.githubusercontent.com/83282165/148902582-e1e32d5a-d0ee-4be5-b416-52cac0c52e96.jpg)


# Project files
* run `python train.py`. It will train the model and save it model format .h5 (keras model). 
* Run `python website.py` to run the website into `http://127.0.0.1:5000/`. 
* `helper.py` is a custom helper function to help load the model and images.
* `db.py` pyhton script to initialise database and `db_models.py` consist of custom db functions 



# Usage

* Clone this repo `git clone https://github.com/Shihabaln/flask_almond_classifier.git`
* Python dependencies `pip install -r requirements.txt`
* To install scikit-image `python -m pip install -U scikit-image `
* `saved_model.h5` will contain the model parameters 
*`images.db` can be created by `form db import db` then `db.create_all()`
*  Upload a picture and let the App predict it 


