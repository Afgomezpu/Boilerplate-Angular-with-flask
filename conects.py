from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
# conectar a la base de datos a mongo
mongo1 = PyMongo(app, uri="mongodb://localhost:27017/pythonmongodbs")

# connectar a otra base de datos con el mismo host
mongo2 = PyMongo(app, uri="mongodb://localhost:27017/myDatabase")

# conectar a otro servidor mongo
mongo3 = PyMongo(app, uri="mongodb://another.host:27017/databaseThree")