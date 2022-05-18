from db import db 
import sqlite3
from sqlite3 import Error

# create db model 
class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    
 #A function to return a string when we add something
    def __repr__(self):
        return '<image id={},name={}>'.format(self.id, self.name)

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_image(conn,name):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return: filename object
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM images WHERE name=?", (name,))
    rows = cur.fetchall()

    for row in rows:
        # print("Id = ", row[0], "Name = ", row[1])
        # name = row[1]
        return row[1]

    cur.close

# Function to add images name to db
def add_image(image_dict):
    new_image = Image(name=image_dict['name'])
    db.session.add(new_image)
    db.session.commit()

