from flask import Blueprint, Flask, jsonify
from app.api.v2.models.question_models import AddQuestion
from app.validators.token_validation import token_required

#set up vote views blueprints
vt_two = Blueprint('vote_api', __name__)

class VoteOnQuestions:
    """ Defines the upvote route """
    @vt_two.route('/v2/<int:question_id>/upvote', methods = ['PATCH'])
    @token_required
    def upvote_question(user_id, question_id):
        """ defines question upvote """
        all_questions = AddQuestion.get_questions()
        for question in all_questions:            
            if question['id'] == question_id:
                votes = question['votes'] + 1
                updated_qsn = AddQuestion.update_question(votes,question_id)
                return jsonify({
                    'status': 200,
                    'data':[{
                        'question':question['id'],
                        'title':question['title'],
                        'body':question['body'],
                        'votes': votes,
                        'updated Question': updated_qsn
                    }]
                }), 200
        return jsonify({
            'status': 404,
            "message":"question not found"
        }), 404
    
    @vt_two.route('/v2/<int:question_id>/downvote', methods = ['PATCH'])
    @token_required
    def down_question(user_id, question_id):
        """ Defines the downvote route """
        all_questions = AddQuestion.get_questions()
        for question in all_questions:            
            if question['id'] == question_id:
                votes = question['votes']
                if votes > 0:
                    votes = votes - 1
                updated_qsn = AddQuestion.update_question(votes,question_id)
                return jsonify({
                    'status': 200,
                    'data':[{
                        'question':question['id'],
                        'title':question['title'],
                        'body':question['body'],
                        'votes': votes
                    }]
                }), 200
            else:
                return jsonify({
                    'status': 404,
                    "message":"question not found"
                }), 404