from flask import Blueprint, Flask, jsonify, request, redirect
from app.api.v1.models.user_models import UserInfo, MeetupInfo, AddQuestion, FetchMeetup

mod = Blueprint('api', __name__)

@mod.route("/v1/users", methods = ['GET'])
def order():
    a = UserInfo({},'')
    b = a.eachUser()
    return jsonify({
        'users':b
    })

@mod.route('/v1/user/auth/signup', methods = ['POST'])
def user_signup():
    user = request.get_json("user")
    a = UserInfo(user,'')
    b = a.eachUser()
    return jsonify({
        'users':b
    })

@mod.route('/v1/user/auth/login/<int:user_id>', methods = ['GET'])
def user_login(user_id):
    c = UserInfo('',user_id)
    d = c.specificUser()
    return jsonify({
        'users':d
    })

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
    return jsonify({
        'meetups':meetups
    })


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
    return jsonify({
        'Question':questions
    })

@mod.route('/v1/meetups/<int:meetup_id>', methods = ['GET'])
def get_meetup(meetup_id):
    meetup = FetchMeetup(meetup_id)
    add_meetup = meetup.get_meetup()
    return jsonify({
        'meetup':add_meetup
    })

@mod.route('/v1/get_meetups', methods = ['GET'])
def get_meetups():
    meetup = FetchMeetup('')
    fetch_meetups = meetup.get_all_meetups()
    return jsonify({
        'meetups':fetch_meetups
    })