# from flask import Flask

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///images.db'
# from flask_sqlalchemy import SQLAlchemy

# #intialize the database
# db = SQLAlchemy(app)

# # create db model 
# class Image(db.Model):
#     __tablename__ = 'images'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String())
#     img_filename = db.Column(db.String())
#     img_data = db.Column(db.LargeBinary)


#  #A function to return a string when we add something
#     def __repr__(self):
#         return '<image id={},name={}>'.format(self.id, self.name)
# @app.route('/')
# def hello_world():
#     return "Hello world, this is going to a web browser"

# # app.run()