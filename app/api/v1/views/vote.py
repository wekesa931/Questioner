from flask import Blueprint, Flask, jsonify
from app.api.v1.models.question_models import AddQuestion

vt = Blueprint('vote_api', __name__)

class VoteOnQuestions:
    
    @vt.route('/v1/<int:question_id>/upvote', methods = ['PATCH'])
    def upvote_question(question_id):
        question = AddQuestion.get_question(question_id)
        if question == {}:
            return jsonify({"message":"question not found"}), 404
        votes = question['votes'] + 1
        return jsonify({
            'question':question['id'],
            'title':question['title'],
            'body':question['body'],
            'votes': votes
        }), 200
        AddQuestion.update_question_upvote(question_id)
    
    @vt.route('/v1/<int:question_id>/downvote', methods = ['PATCH'])
    def down_question(question_id):
        question = AddQuestion.get_question(question_id)
        if question == {}:
            return jsonify({"message":"question not found"}), 404
        votes = question['votes']
        if votes > 0:
            votes = votes - 1
        return jsonify({
            'status': '200',
            'data':[{
                'question':question['id'],
                'title':question['title'],
                'body':question['body'],
                'votes': votes
            }]
        }), 201
        AddQuestion.update_question_downvote(question_id)