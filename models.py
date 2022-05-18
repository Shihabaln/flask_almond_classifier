from flask_sqlalchemy import SQLAlchemy

#intialize the database
db = SQLAlchemy()

# create db model 
class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    img_data = db.Column(db.LargeBinary)


 #A function to return a string when we add something
    def __repr__(self):
        return '<image id={},name={}>'.format(self.id, self.name)

# Function to commit image to db
def add_image(image_dict):
    new_image = Image(name=image_dict['name'], \
                        img_data=image_dict['img_data'])
    db.session.add(new_image)
    db.session.commit()