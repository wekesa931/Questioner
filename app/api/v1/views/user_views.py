from flask import Blueprint, Flask, jsonify, request, redirect
from app.api.v1.models.user_models import UserInfo

mod = Blueprint('api', __name__)

@mod.route("/", methods = ['GET'])
def order():
    a = UserInfo({})
    b = a.eachUser()
    return jsonify({
        'users':b
    })

@mod.route('/v1/user/auth/signup', methods = ['POST'])
def addOne():
    user = request.get_json("item")
    a = UserInfo(user)
    b = a.eachUser()
    return jsonify({
        'users':b
    })