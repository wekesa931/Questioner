from flask import Blueprint, Flask, jsonify
from app.api.v1.models.question_models import AddQuestion

vt = Blueprint('vote_api', __name__)

class VoteOnQuestions:
    
    @vt.route('/v1/<int:question_id>/upvote', methods = ['PATCH'])
    def upvote_question(question_id):
        question = AddQuestion.get_question(question_id)
        votes = question['votes'] + 1
        response = jsonify({
            'question':question['id'],
            'title':question['title'],
            'body':question['body'],
            'votes': votes
        })
        response.status_code = 200
        return response   

    
    @vt.route('/v1/<int:question_id>/downvote', methods = ['PATCH'])
    def down_question(question_id):
        question = AddQuestion.get_question(question_id)
        votes = question['votes']
        if votes > 0:
            votes = votes - 1
        response = jsonify({
            'question':question['id'],
            'title':question['title'],
            'body':question['body'],
            'votes': votes
        })
        response.status_code = 200
        return response    
    