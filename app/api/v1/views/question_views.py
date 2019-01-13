from flask import Blueprint, Flask, jsonify, request
from app.api.v1.models.question_models import AddQuestion
from app.api.v1.models.meetup_models import MeetupInfo
from app.validators.shared_validators import check_fields

#set up question views blueprints
qsn = Blueprint('questions_api', __name__)

class QuestionsVIews:
    """ Defines the question route """
    @qsn.route('/v1/<int:meetup_id>/post_question', methods = ['POST'])
    def post_question(meetup_id):
        """ fetch the posted information from the user input """
        meetup = MeetupInfo
        get_meetup = meetup.get_meetup(meetup_id) 
        if get_meetup == {}:
            return jsonify({
                "message":"meetup not found"
            }), 404
        question = request.get_json("question")
        #validate obtained information
        validate_info = ['title','body']
        error = check_fields(question, validate_info)
        if len(error) > 0:
            return jsonify({
                "message":error
            }), 400
        title = question['title']
        body = question['body']
        question_object = AddQuestion('',meetup_id,title,body)
        questions = question_object.add_question()
        return jsonify({
            'status': '201',
            'data':[{
                'Questions':questions
            }]
        }), 201