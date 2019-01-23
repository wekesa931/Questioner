from flask import jsonify
from app.api.v2.models.meetup_models import MeetupInfo

def check_valid(location,topic,happeningOn):
    error_message = {}
    all_meetups = MeetupInfo.get_meetups()
    for meetup in all_meetups:
        if meetup['happeningon'].strftime('%Y-%m-%d') == happeningOn:
            print('yes')
            if meetup['location'] == location:
                error_message['key error'] = "Another meetup is happening on the same location!"
            elif meetup['topic'] == topic:
                error_message['key error'] = "Another meetup has the same topic!"
    return error_message