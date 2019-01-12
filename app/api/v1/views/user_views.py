from flask import Blueprint, Flask, jsonify, request
from app.api.v1.models.user_models import UserInfo 
from app.validators.user_validators import Validators

validate = Validators()

mod = Blueprint('api', __name__)

class UserViews:
    @mod.route('/v1/user/auth/all_users', methods = ['GET'])
    def get_all_users():
        user = UserInfo
        all_users = user.get_all_users()
        response = jsonify({
            'users':all_users
        })
        response.status_code = 200
        return response

    @mod.route('/v1/user/auth/signup', methods = ['POST'])
    def user_signup():
        user_info = request.get_json("user")
        if not user_info:
            return jsonify({"message":"No data found"}), 400
        firstname = user_info['firstname']
        lastname = user_info['lastname']
        othername = user_info['othername']
        username = user_info['username']
        email = user_info['email']
        phoneNumber = user_info['phoneNumber']
        password = user_info['password']

        if not all(val in user_info for val in [
                                "firstname",
                                "lastname", 
                                "othername", 
                                "username",
                                "email",
                                "phoneNumber",
                                "password"]):
            return jsonify({"message":"Some fields are missing"}), 400
        if not validate.check_password(password):
            return jsonify({"message":"password is not valid"}), 400
        if not validate.check_email(email):
            return jsonify({"message":"email is not valid"}), 400
        if validate.check_repeated(username):
            return jsonify({"message":"username taken!"}), 400
        if validate.check_repeated(email):
            return jsonify({"message":"email taken!"}), 400
        

        user = UserInfo(
                            '',
                            firstname,
                            lastname,
                            othername,
                            username,
                            email,
                            phoneNumber,
                            password
                        )

        users_db = user.eachUser()
        response = jsonify({
            'users':users_db
        })
        response.status_code = 201
        return response

    @mod.route('/v1/user/auth/login/<int:user_id>', methods = ['GET'])
    def user_login(user_id):
        user = UserInfo
        each_user = user.get_user(user_id)
        response = jsonify({
            'users':each_user
        })
        response.status_code = 200
        return response