from flask import Blueprint, Flask, jsonify
from app.api.v1.models.question_models import AddQuestion
from app.validators.token_validation import token_required

#set up vote views blueprints
vt = Blueprint('vote_api', __name__)

class VoteOnQuestions:
    """ Defines the upvote route """
    @vt.route('/v1/<int:question_id>/upvote', methods = ['PATCH'])
    @token_required
    def upvote_question(user_id, question_id):
        """ defines question upvote """
        question = AddQuestion.get_question(question_id)
        #handle validation
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
    @token_required
    def down_question(user_id, question_id):
        """ Defines the downvote route """
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
        }), 200