from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world, this is going to a web browser"

app.run()