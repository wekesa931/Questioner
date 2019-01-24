from flask import jsonify
from app.api.v2.models.meetup_models import MeetupInfo
from app.api.v2.models.question_models import AddQuestion

def check_valid(location,topic,happeningOn):
    error_message = {}
    all_meetups = MeetupInfo.get_meetups()
    for meetup in all_meetups:
        if meetup['happeningon'].strftime('%Y-%m-%d') == happeningOn:
            if meetup['location'] == location:
                error_message['key error'] = "Another meetup is happening on the same location!"
            elif meetup['topic'] == topic:
                error_message['key error'] = "Another meetup has the same topic!"
    return error_message

def check_valid_qsn(title,body):
    error_message = {}
    all_question = AddQuestion.get_questions()
    for question in all_question:
        if question['title'] == title:
            error_message['key error'] = "A question with that title already exists in this meetup!"
        elif question['body'] == body:
            error_message['key error'] = "A similar question exists in this meetup!"
    return error_message