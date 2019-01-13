from flask import Blueprint, Flask, jsonify, request
from app.api.v1.models.question_models import AddQuestion
from app.api.v1.models.meetup_models import MeetupInfo

qsn = Blueprint('questions_api', __name__)

class QuestionsVIews:
    @qsn.route('/v1/<int:meetup_id>/post_question', methods = ['POST'])
    def post_question(meetup_id):


        meetup = MeetupInfo
        get_meetup = meetup.get_meetup(meetup_id) 
        if get_meetup == {}:
            return jsonify({
                "message":"meetup not found"
            }), 404
        
        
        question = request.get_json("question")
        if not question:
            return jsonify({
                "message":"No body given"
            }), 400
        createdOn = question['createdOn']
        title = question['title']
        body = question['body']
        question_object = AddQuestion(
                            '',
                            createdOn,
                            meetup_id,
                            title,
                            body
                        )
        questions = question_object.add_question()
        response = jsonify({
            'Questions':questions
        })
        response.status_code = 201
        return response