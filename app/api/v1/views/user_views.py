from flask import Blueprint, Flask, jsonify, request, redirect
from app.api.v1.models.user_models import UserInfo 

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
        firstname = user_info['firstname']
        lastname = user_info['lastname']
        othername = user_info['othername']
        email = user_info['email']
        phoneNumber = user_info['phoneNumber']
        password = user_info['password']
        user = UserInfo(
                            '',
                            firstname,
                            lastname,
                            othername,
                            email,
                            phoneNumber,
                            password
                        )

        all_users = user.eachUser()
        response = jsonify({
            'users':all_users
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