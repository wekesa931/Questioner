from flask import Blueprint, Flask, jsonify, request, redirect
from app.api.v1.models.user_models import UserInfo 
from app.api.v1.models.meetup_models import MeetupInfo
from app.api.v1.models.question_models import AddQuestion

mod = Blueprint('api', __name__)

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

@mod.route('/v1/add_meetups', methods = ['POST'])
def create_meetup():
    meetup = request.get_json("meetups")
    createdOn = meetup['createdOn']
    location = meetup['location']
    images = meetup['images']
    topics = meetup['topics']
    happeningOn = meetup['happeningOn']
    tags = meetup['tags']
    meetup_object = MeetupInfo(
                        '',
                        createdOn,
                        location,
                        topics,
                        happeningOn,
                        tags,
                        images
                        )
    meetups = meetup_object.add_meetup()
    response = jsonify({
        'meetups':meetups
    })
    response.status_code = 201
    return response

@mod.route('/v1/post_question', methods = ['POST'])
def post_question():
    question = request.get_json("question")
    createdOn = question['createdOn']
    meetup = question['meetup']
    title = question['title']
    body = question['body']
    votes = question['votes']
    question_object = AddQuestion(
                        '',
                        createdOn,
                        meetup,
                        title,
                        body,
                        votes
                    )
    questions = question_object.add_question()
    response = jsonify({
        'Questions':questions
    })
    response.status_code = 201
    return response

@mod.route('/v1/meetups/<int:meetup_id>', methods = ['GET'])
def get_meetup(meetup_id):
    meetup = MeetupInfo
    get_meetup = meetup.get_meetup(meetup_id)
    response = jsonify({
        'meetup':get_meetup
    })
    response.status_code = 200
    return response

@mod.route('/v1/get_meetups', methods = ['GET'])
def get_meetups():
    meetup = MeetupInfo
    fetch_meetups = meetup.get_all_meetups()
    response = jsonify({
         'meetups':fetch_meetups
    })
    response.status_code = 200
    return response