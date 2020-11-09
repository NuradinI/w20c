from flask import Flask, request, Response
import mariadb
import json
app = Flask(__name__)

@app.route('/getAnimals',  methods=['GET'])
def animal():
    animals = ['lion', 'duck', 'pig', 'cow', 'kitten', 'dog']
    return Response(json.dumps(animals), mimetype='application/json', status=200)

@app.route('/postAnimal', methods=['POST'])
def postAnimal():
    animals = ['lion', 'duck', 'pig', 'cow', 'kitten', 'dog']
    animals.append('snake')
    return Response( json.dumps(animals), mimetype='text/html', status=200)

@app.route('/patchAnimal', methods=['PATCH'])
def patchAnimal():
    animals = ['lion', 'duck', 'pig', 'cow', 'kitten', 'dog']
    animals[4] = 'cat'
    return Response(json.dumps(animals), mimetype='text/html', status=200)

@app.route('/deleteAnimal', methods=['DELETE'])
def deleteAnimal():
    animals = ['lion', 'duck', 'pig', 'cow', 'kitten', 'dog', 'mouse']
    animals.remove('pig')
    return Response(json.dumps(animals), mimetype='text/html', status=200)
    