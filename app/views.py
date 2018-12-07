from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token
# from flask_jwt_extended import get_jwt_identity, jwt_required
"""This module handles the signup route"""
from flask import jsonify, make_response, request
import flask.views
from werkzeug.security import generate_password_hash
from flasgger import swag_from
from app.helper import (is_not_valid_username,\
                        is_not_valid_password, validate_not_email_structure,\
                        is_not_valid_role, validate_not_keys)
from .models import User
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity

app = Flask(__name__)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'mybuangels'


@app.route('/', methods=['GET'])
def index():
    return "here hyhagain"

@app.route('/api/v1/signup', methods=['POST'])
def signup():
    """Method handling the user signup route"""
    print(request.get_json())
    try:
        parser = request.get_json()

        if validate_not_keys(parser,4):
            return make_response(jsonify({"message": "Some fields are missing!"}),400)
        username = parser.get('username')
        password = parser.get('password')
        email = parser.get('email')
        role = parser.get('role')
        
        if is_not_valid_username(username.strip()):
            return make_response(jsonify({"message": "Please supply a username\
            of 4 or more characters"}), 400)
        if is_not_valid_password(password.strip()):
            return make_response(jsonify({"message": "Password is incorrect"}), 400)
        if is_not_valid_role(role.strip()):
            return make_response(jsonify({"message": "role is incorrect"}), 400)
        if validate_not_email_structure(email.strip()):
            return make_response(jsonify({"message": "email is incorrect"}), 400)
       
        use = User(username.lower(), email, password, role)
        user = use.check_user(username)
        if user:
            return make_response(jsonify({'message': 'Username already exists'}), 403)
        use.insert_user_data()
        usee =use.fetch_user(username)
        access_token = create_access_token(identity={"username": username})
        # response = {"details":use.get_dictionary(), 'message': "you have succesfully signed up" }
        # return make_response(jsonify({'message': "you have succesfully signed up"}), 201)

        return jsonify({'token':access_token, 'message': "you have succesfully signed up", 'user':usee})
    except Exception as error:
        raise error

# @app.route('/api/v1/login', methods=['POST'])
# def login():
#     print(request.get_json())
#     try:
#         parser = request.get_json()

#         if validate_not_keys(parser,2):
#             return make_response(jsonify({"message": "Some fields are missing!"}),400)
#         username = parser.get('username')
#         password = parser.get('password')




@app.route('/api/v1/users', methods=['GET'])
@jwt_required
def getusers():
    use = User(username = None, email = None, password = None, role = None)
    return jsonify(use.fetch_all_users())