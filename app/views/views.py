from conects import mongo1, mongo2
from flask import Flask, jsonify,request,Response,render_template,Blueprint
from bson import json_util
from bson.json_util import loads, dumps
from bson.objectid import ObjectId
from flask_cors import CORS, cross_origin
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

blueprint = Blueprint('views', __name__)


#se genera la ruta principal con una peticion get
@blueprint.route('/')
def home():
    return jsonify({"msg": "Missing JSON in request"}), 400 

#se genera la ruta login con una peticion post y responde con el token si todo esta bien 
@blueprint.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    correo = request.json.get('correo', None)
    contrasena = request.json.get('contrasena', None)
    if not correo:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not contrasena:
        return jsonify({"msg": "Missing password parameter"}), 400
    if correo and contrasena:
        consulta=mongo1.db.users.find_one({"correo":correo})
        json_str = dumps(consulta)
        record2 = loads(json_str)
        if record2["correo"]==correo and record2["contrasena"]==contrasena:
            token = create_access_token(identity=correo)
            return jsonify(token=token), 200
        else:
            return jsonify({'ingreso':'fallido'})
    

#se genera la ruta restaurar contraña con una peticion post con el token en el encabezado para realizar la resutacion de 
#contraseña
@blueprint.route('/restaurarcontrasena', methods=['POST'])
@jwt_required
def restaurarcontrasena():
    contrasena = request.json.get('contrasena', None)
    current_user = get_jwt_identity()
    myquery = { "correo":current_user}
    newvalues = { "$set": { "contrasena":contrasena } }
    if contrasena:
       mongo1.db.users.update(myquery, newvalues)
    
    return jsonify(logged_in_as=current_user), 200
    
#ruta users con post nos permite ingresar el usuario 
@blueprint.route('/users', methods=['POST'])
def create_user():
    
    nombre= request.json['nombre']
    apellido= request.json['apellido']
    correo= request.json['correo']
    contrasena =request.json['contrasena']
    
    if nombre and apellido and correo and contrasena:
        id = mongo1.db.users.insert({"nombre" : nombre,"apellido" :apellido,"correo" : correo , "contrasena":contrasena })
        return str(id)
    else:
        return jsonify({"msg": "informacion incompleta"})
        

#ruta users con get nos permite tener todos los usuarios
@blueprint.route('/users', methods=['GET'])
def get_users():
    users=mongo1.db.users.find()
    response=json_util.dumps(users)
    return Response(response,mimetype='application/json')


#ruta users/<correo> nos permite eliminar un usuario con un unico correo
@blueprint.route('/users/<correo>', methods=['DELETE'])
def eliminar(correo):
    mongo1.db.users.delete_one({'correo':correo})
    return 'eliminado'
    
