from flask import Flask, request as req
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from app.views import views

# se crea el microfamework flask
app = Flask(__name__)
app.register_blueprint(views.blueprint)
app.config['JWT_SECRET_KEY'] = 'super-secret' 
jwt = JWTManager(app)
