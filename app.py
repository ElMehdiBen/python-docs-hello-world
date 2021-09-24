from flask import Flask
import random
import numpy as np

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
    liste = ["Camille", "Olivier", "Laurent", "Pascal", "Ludwig", "Noura","Anne-Charlotte","Charlène", "Malick","Tristan","Zeyno"]
    random.shuffle(liste) #permet de mélanger la liste de façon aléatoire
    ar = np.array(liste) # transformation de la liste en array
    listegroup=np.array_split(ar,n)
    groups = {}
    i = 1
    for l in listegroup:
        key = "Groupe " + str(i)
        groups[key] = list(l)
        i+=1
    return groups
