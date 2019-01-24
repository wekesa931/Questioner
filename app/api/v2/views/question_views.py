from flask import Blueprint, Flask, jsonify, request
from app.api.v2.models.question_models import AddQuestion
from app.api.v2.models.meetup_models import MeetupInfo
from app.api.v2.models.comments_models import AddComment
from app.validators.shared_validators import check_fields
from app.validators.token_validation import token_required
from app.validators.repeat_validation import check_valid_qsn

#set up question views blueprints
qsn_two = Blueprint('questions_api', __name__)

class QuestionsVIews:
    """ Defines the question route """
    @qsn_two.route('/v2/<int:meetup_id>/post_question', methods = ['POST'])
    @token_required
    def post_question(meetup_id,is_admin,user_id):
        """ fetch the posted information from the user input """
        all_meetups = MeetupInfo.get_meetups()
        for meetup in all_meetups:
            if meetup['id'] == meetup_id:
                question = request.get_json("question")
                validate_info = ['title','body']
                error = check_fields(question, validate_info)
                if len(error) > 0:
                    return jsonify({
                        "status": 400,
                        "message":error
                    }), 400
                title = question['title']
                body = question['body']
                question_validation = check_valid_qsn(title,body)
                if len(question_validation) > 0:
                    return jsonify({
                        "status": 400,
                        "message":question_validation
                    }), 400
                question_object = AddQuestion(user_id,meetup_id,title,body)
                questions = question_object.add_question()
                return jsonify({
                    'status': 201,
                    'data':[{
                        'Questions':questions
                    }]
                }), 201
        return jsonify({
            "status": 404,
            "message":"No metups found"
        }), 404

    @qsn_two.route('/v2/<int:meetup_id>/get_all_questions', methods = ['GET'])
    @token_required
    def get_all_question(meetup_id,is_admin,user_id):
        all_questions = AddQuestion.get_questions()
        all_meetups = MeetupInfo.get_meetups()
        if len(all_meetups) == 0:
            return jsonify({
                'status': 404,
                'data':[{
                    'message':'meetup not found'
                }]
            }), 404
        all_meetup_questions = {}
        for question in all_questions:
            if question['meetup_id'] == meetup_id:
                all_meetup_questions.update({'question {}'.format(len(all_meetup_questions)):question})
        if len(all_meetup_questions) == 0:
            return jsonify({
                'status': 404,
                'message':'Questions not found'
            }), 404
        return jsonify({
            'status': 200,
            'data':[{
                'questions':all_meetup_questions
            }]
        }), 200
       
    @qsn_two.route('/v2/<int:question_id>/comment', methods = ['POST'])
    @token_required
    def post_comment(user_id, is_admin,question_id):
        all_questions = AddQuestion.get_questions()
        for question in all_questions:
            if question['id'] == question_id:
                comment = request.get_json("comment")
                validate_info = ['comment']
                error = check_fields(comment, validate_info)
                if len(error) > 0:
                    return jsonify({
                        'status': 400,
                        'message':error
                    }), 400
                my_comment = comment['comment']
                comment_object = AddComment(user_id,question_id,my_comment)
                comments = comment_object.add_comment()
                com = comments['comments']
                cdon = comments['createdon']
                return jsonify({
                        'status': 201,
                        'data':[{
                            'Question':question,
                            'comment':{
                                'Comment':com,
                                'Created On':cdon
                            }
                        }]
                    }), 201
        return jsonify({
            'status': 404,
            'message':'Question not found'
        }), 404
    
    @qsn_two.route('/v2/<int:question_id>/get_qsn', methods = ['GET'])
    @token_required
    def get_qsn(user_id, is_admin,question_id):
        question = AddQuestion.get_one_question(question_id)
        if question == False:
            return jsonify({
                'status': 400,
                'data':[{
                    'message': 'Question not found'
                }]
            })
        all_comments = AddComment.get_comments()
        comment_list = []
        for comment in all_comments:
            if comment['question_id']== question_id:
                body = [comment['comments'],
                        comment['user_id']]
                comment_list.append(body)
        return jsonify({
            'status': 200,
            'data':[{
                'question': question,
                'comments': comment_list
            }]
        })