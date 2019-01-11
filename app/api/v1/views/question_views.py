from flask import Blueprint, Flask, jsonify, request
from app.api.v1.models.question_models import AddQuestion

qsn = Blueprint('questions_api', __name__)

class QuestionsVIews:
    @qsn.route('/v1/post_question', methods = ['POST'])
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