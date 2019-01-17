from flask import Blueprint, Flask, jsonify, request
from app.api.v2.models.question_models import AddQuestion
from app.api.v2.models.meetup_models import MeetupInfo
from app.validators.shared_validators import check_fields
from app.validators.token_validation import token_required

#set up question views blueprints
qsn_two = Blueprint('questions_api', __name__)

class QuestionsVIews:
    """ Defines the question route """
    @qsn_two.route('/v2/<int:meetup_id>/post_question', methods = ['POST'])
    @token_required
    def post_question(meetup_id, user_id):
        """ fetch the posted information from the user input """
        all_meetups = MeetupInfo.get_meetups()
        for meetup in all_meetups:
            if meetup['id'] == meetup_id:
                question = request.get_json("question")
                validate_info = ['title','body']
                error = check_fields(question, validate_info)
                if len(error) > 0:
                    return jsonify({
                        "message":error
                    }), 400
                title = question['title']
                body = question['body']
                question_object = AddQuestion(user_id,meetup_id,title,body)
                questions = question_object.add_question()
                return jsonify({
                    'status': '201',
                    'data':[{
                        'Questions':questions
                    }]
                }), 201
            else:
                return jsonify({
                "message":"meetup not found"
                }), 404