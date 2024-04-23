from flask import Blueprint, request, jsonify
from src.models.usersModel import User
from src.services.AuthService import AuthService
from werkzeug.security import generate_password_hash
from flask import Flask
import pymysql

Auth_blueprint = Blueprint('auth_blueprint', __name__)

@Auth_blueprint.route('/', methods=['POST'])
def login():
    Name_User = request.json['Name_User']
    Password_User = request.json['Password_User']

    user = User(0, Name_User, Password_User, 0, 0)

    authenticated_user = AuthService.login(Name_User, Password_User)

    if authenticated_user:
        encoded_jwt = AuthService.generate_token(authenticated_user)

        return jsonify({'token': encoded_jwt}), 200
    else:
        return jsonify({"mensaje: Usuario o Contraseña incorrecta"}), 401

    
    