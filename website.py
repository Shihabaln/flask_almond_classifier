# Two main categories
X = "Normal"
Y = "Broken"

# images to be displayed 
sampleX='static/g15normal277.png'
sampleY='static/g15broken4.png'

# Storing files in this folder
Upload_folder = 'static/uploads'
# Allowed files
Allowed_files = {'png', 'jpg', 'jpeg', 'gif'}
# Machine Learning Model Filename
Model_name = 'saved_model.h5'

#Load operation system library
import os
from io import BytesIO
from unicodedata import name
basedir = os.path.abspath(os.path.dirname(__file__))

#website libraries
from flask import render_template
from flask import Flask, flash, request, redirect, url_for
from flask_migrate import Migrate
from werkzeug.utils import secure_filename

#ML libraries
from keras.preprocessing import image
from keras.models import load_model
from keras.backend import set_session
import tensorflow as tf

# resize image 
import PIL.Image
import numpy as np
from skimage import transform

from flask_sqlalchemy import SQLAlchemy
from db import db_init, db
from db_models import Image, add_image, create_connection, select_image

# Create the website object
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db_init(app)
migrate = Migrate(app,db)

def load_model_from_file():
    #Set up the machine learning session
    mySession = tf.compat.v1.Session()
    set_session(mySession)
    myModel = load_model(Model_name)
    myGraph = tf.compat.v1.get_default_graph()
    return (mySession,myModel,myGraph)

# Function to resize input to predection 
def load(filename):
   np_image = PIL.Image.open(filename)
   np_image = np.array(np_image).astype('float32')/255
   np_image = transform.resize(np_image, (150, 150, 3))
   np_image = np.expand_dims(np_image, axis=0)
   return np_image

#To allow only images
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Allowed_files

#Define the view for the top level page
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    #Initial webpage load
    if request.method == 'GET' :
        return render_template('index.html',myX=X,myY=Y,mySampleX=sampleX,mySampleY=sampleY)
    else: # if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser may also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        # If it doesn't look like an image file
        if not allowed_file(file.filename):
            flash('I only accept files of type'+str(Allowed_files))
            return redirect(request.url)
        #When the user uploads a file with good parameters
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            add_image({
                'name': file.filename})
            file.save(os.path.join(app.config['Upload_folder'], filename))
            # flash('New image "{}" created.'.format(request.form['name']))
            
            return redirect(url_for('uploaded_file', filename=filename))

    
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    #load image with requested image size 
    # image_query = Image.query.filter_by(name=filename).first_or_404()
    conn = create_connection(database)
    file_name = select_image(conn,filename)
    test_image = load(Upload_folder+"/"+file_name)


    mySession = app.config['SESSION']
    myModel = app.config['MODEL']
    myGraph = app.config['GRAPH']
    with mySession.as_default():
        with myGraph.as_default():
            mySession = tf.compat.v1.Session()
            myModel = load_model(Model_name)
            myGraph = tf.compat.v1.get_default_graph()
            set_session(mySession)
            result = myModel.predict(test_image)
            # image_src = Image.query.filter_by(name=filename).first_or_404()
            image_src = "/"+Upload_folder +"/"+file_name
            if result[0] < 0.5 :
                answer = "<div class='col text-center'><img width='150' height='150' src='"+image_src+"' class='img-thumbnail' /><h4>guess:"+Y+" "+str(result[0])+"</h4></div><div class='col'></div><div class='w-100'></div>"     
            else:
                answer = "<div class='col'></div><div class='col text-center'><img width='150' height='150' src='"+image_src+"' class='img-thumbnail' /><h4>guess:"+X+" "+str(result[0])+"</h4></div><div class='w-100'></div>"     
            results.append(answer)
            return render_template('index.html',myX=X,myY=Y,mySampleX=sampleX,mySampleY=sampleY,len=len(results),results=results)
    


def main():
    (mySession,myModel,myGraph) = load_model_from_file()
    
    app.config['SECRET_KEY'] = 'super secret key'

    #Debuggin On
    config = {"DEBUG": True }
    app.config.from_mapping(config)
    
    #dict fot configurations
    app.config['SESSION'] = mySession
    app.config['MODEL'] = myModel
    app.config['GRAPH'] = myGraph

    app.config['Upload_folder'] = Upload_folder
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #16MB upload limit
    app.run()

# Create a running list of results
results = []

#Launch everything
main()
