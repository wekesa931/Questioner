from flask import Blueprint, Flask, jsonify, request
from app.api.v1.models.user_models import UserInfo 
from app.validators.user_validators import Validators
from app.validators.shared_validators import check_fields


validate = Validators()

mod = Blueprint('api', __name__)

class UserViews:
    @mod.route('/v1/user/auth/all_users', methods = ['GET'])
    def get_all_users():
        user = UserInfo
        all_users = user.get_all_users()
        return jsonify({
            'users':all_users
        }), 200

    @mod.route('/v1/user/auth/signup', methods = ['POST'])
    def user_signup():
        user_info = request.get_json("user")
        validate_info = ['firstname','lastname','othername','username','email','phoneNumber','password']
        error = check_fields(user_info, validate_info)
        if len(error) > 0:
            return jsonify({
                "message":error
            }), 400
        firstname = user_info['firstname']
        lastname = user_info['lastname']
        othername = user_info['othername']
        username = user_info['username']
        email = user_info['email']
        phoneNumber = user_info['phoneNumber']
        password = user_info['password']
        
        if not validate.check_password(password):
            return jsonify({"message":"password is not valid"}), 400
        if not validate.check_email(email):
            return jsonify({"message":"email is not valid"}), 400
        if validate.check_repeated(username):
            return jsonify({"message":"username taken!"}), 400
        if validate.check_repeated(email):
            return jsonify({"message":"email taken!"}), 400
        user = UserInfo('', firstname, lastname, othername, username, email, phoneNumber, password)
        users_db = user.eachUser()
        return jsonify({
            'status': '201',
            'data':[{
                'users':users_db
            }]
        }), 201

    @mod.route('/v1/user/auth/login/<int:user_id>', methods = ['GET'])
    def user_login(user_id):
        user = UserInfo
        each_user = user.get_user(user_id)
        return jsonify({
            'status': '200',
            'data':[{
                'users':each_user
            }]
        }), 201