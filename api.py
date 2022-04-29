import flask
import json
from flask import request, jsonify
from mammals import *
from birds import *


app = flask.Flask(__name__)


def return_animal_list():
    pep = Cat("pep", 10, "Black")
    arsene = Dog("arsene", 7, "White")
    bruce = Bat("bruce", 20, "Black")
    tweetie = Pigeon("tweetie", 3, "Grey")
    stewie = Penguin("stewie", 8, "White")


    animal_list = [pep, arsene, bruce, tweetie, stewie]
    return animal_list


app.config["DEBUG"] = True
animals = return_animal_list()
animals_JSON = []

file = open("petowners.JSON")
PetOwners = json.load(file)

for i, animal in enumerate(animals):
    animals_JSON_iter = {
        'id': i,
        'name': animal.name,
        'age': animal.age,
        'colour': animal.colour,
        
    }
    animals_JSON.append(animals_JSON_iter)


@app.route('/', methods=['GET'])
def home():
    return (
        "<h1>Welcome to our Vet!</h1>"
        "<h2>We are here to help</h2>"
    
    )


@app.route('/api/customers/', methods=['GET'])
def api_all():
    return jsonify(petowners)


@app.route('/api/customers/<int:owner_id>', methods=['GET'])
def return_owner(owner_id):
    if owner_id >= len(petowners):
        return "<h1>Try again</h1>"

    results = []

    for p_id in petowners:
        if int(p_id['id']) == int(owner_id):
            results.append(p_id)

    return jsonify(results)


@app.route('/api/')
def redirect():
    return "<h1><a href='/api/animals')>Animals</a> <br><br> <a href='/api/customers')>Customers</a></h1>"


@app.route('/api/animals/', methods=['GET'])
def list_all_animals():
    return jsonify(animals_JSON)



app.run()
