from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"



@app.route("/docs")
def docs():
    return "This is our API documentation"
