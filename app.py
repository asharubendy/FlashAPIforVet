import flask
import json
from pathlib import Path
from flask import request, jsonify, Flask
from mammals import *
from birds import *


app = flask.Flask(__name__)


def return_animal_list():
    Pep = Cat("Pep", 10, "Black")
    Arsene = Dog("Arsene", 7, "White")
    Bruce = Bat("Bruce", 20, "Black")
    Tweetie = Pigeon("Tweetie", 3, "Grey")
    Stewie = Penguin("Stewie", 8, "White")
    Tom = Cat("Tom", 9, "Ginger")
    Spike = Dog("Spike", 15, "Brown")
    Icy = Penguin("Icy", 6, "White")

    animal_list = [Pep, Arsene, Bruce, Tweetie, Stewie, Tom, Spike, Icy]
    return animal_list


app.config["DEBUG"] = True
animals = return_animal_list()
animals_JSON = []

file = open(Path('petowners.json'))
PetOwners = json.load(file)

for i, animal in enumerate(animals):
    animals_JSON_iter = {
        'name': animal.name,
        'id': i,
        'colour': animal.colour,
        'age': animal.age,
        
    }
    animals_JSON.append(animals_JSON_iter)


@app.route('/', methods=['GET'])
def home():
    return (
        "<h1>Welcome to our Vet!</h1>"
        "<h2>We are here to help!</h2>"
        "<h3>We look after a range of animals.</h3>"
        "<p>To browse the animals we currently have: <a href='/api/animals')>CLICK HERE</a>"
        
    )


@app.route('/api/customers/', methods=['GET'])
def api_all(): 
    petowners = []
    return jsonify(petowners)


@app.route('/api/customers/<int:owner_id>', methods=['GET'])
def return_owner(owner_id):
    petowners = []
    if owner_id >= len(petowners):
        return "<h1>Try again</h1>"

    results = []

    for p_id in petowners:
        if int(p_id['id']) == int(owner_id):
            results.append(p_id)

    return jsonify(results)


@app.route('/api/animals/', methods=['GET'])
def list_all_animals():
    return jsonify(animals_JSON)


if __name__ == '__main__':

    app.run()
