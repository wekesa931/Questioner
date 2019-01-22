from flask import Blueprint, Flask, jsonify, request, make_response, current_app
from app.api.v2.models.user_models import UserInfo
from app.validators.user_validators import Validators
from app.validators.shared_validators import check_fields
from werkzeug.security import check_password_hash
import jwt
import datetime


validate = Validators()

#set up user views blueprints
mod_two = Blueprint('api', __name__)

class UserViews:
    """ Defines the user route """
    @mod_two.route('/v2/user/auth/all_users', methods = ['GET'])
    def get_all_users():
        """ fetch all users from the database """
        all_users = UserInfo.get_all_users()
        return jsonify({
            'status': 200,
            'users':all_users
        }), 200

    @mod_two.route('/v2/user/auth/signup', methods = ['POST'])
    def user_signup():
        """ defines user sign up """
        user_info = request.get_json("user")
        all_users = UserInfo.get_all_users()
        isadmin = False
        if len(all_users)==0:
            isadmin = True
        validate_info = ['firstname','lastname','othername','username','email','phoneNumber','password']
        #validate posted information
        error = check_fields(user_info, validate_info)
        if len(error) > 0:
            return jsonify({
                'status': 400,
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
            return jsonify({
                'status': 400,
                "message":"password is not valid"
                }), 400
        if not validate.check_email(email):
            return jsonify({
                'status': 400,
                "message":"email is not valid"
            }), 400
        if validate.check_repeated(username):
            return jsonify({
                'status': 400,
                "message":"username taken!"
            }), 400
        if validate.check_repeated(email):
            return jsonify({
                'status': 400,
                "message":"email taken!"
            }), 400
        user = UserInfo(firstname, lastname, othername, username, email, phoneNumber, password, isadmin)
        users_db = user.add_user()
        return jsonify({
            'status': 201,
            'data':[{
                'users':users_db
            }]
        }), 201

    @mod_two.route('/v2/user/auth/login', methods = ['POST'])
    def user_login():
        user_info = request.get_json("login")
        username = user_info['username']
        password = user_info['password']

        all_users = UserInfo.get_all_users()
        for user in all_users:
            if user['username'] == username:
                if check_password_hash(user['password'], password):
                    secret_key = current_app.config['SECRET']
                    token = jwt.encode({
                        'user_id':user['id'],
                        'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30) 
                        }, secret_key)
                    return jsonify({
                        'status': 200,
                        'data':[{
                            'token':token.decode('UTF-8'),
                            'user': user
                        }]
                    })
                else:
                    return jsonify({
                        'status': 403,
                        'message':'Wrong password!'
                    }), 403 
        return jsonify({
            'status': 404,
            'message':'Username not found!'}), 404  
        