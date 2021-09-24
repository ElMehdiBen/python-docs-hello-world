from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello DataA"

@app.route("/docs")
def docs():
    return "This is the documentation of our API"

@app.route("/id/<id>")
def return_id(id):
    id = int(id) + 10
    return "Here is what was sent : " + str(id)

@app.route("/random/<n>")
def teams(n):
    n = int(n)
    liste = ["Camille", "Olivier", "Laurent", "Charlene"]
    return liste[n]
