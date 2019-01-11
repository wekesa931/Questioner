from flask import Blueprint, Flask, jsonify, request, redirect
from app.api.v1.models.meetup_models import MeetupInfo

mtp = Blueprint('meetup_api', __name__)

class MeetupViews:
    @mtp.route('/v1/add_meetups', methods = ['POST'])
    def create_meetup():
        meetup = request.get_json("meetups")
        createdOn = meetup['createdOn']
        location = meetup['location']
        images = meetup['images']
        topics = meetup['topics']
        happeningOn = meetup['happeningOn']
        tags = meetup['tags']
        meetup_object = MeetupInfo(
                            '',
                            createdOn,
                            location,
                            topics,
                            happeningOn,
                            tags,
                            images
                            )
        meetups = meetup_object.add_meetup()
        response = jsonify({
            'meetups':meetups
        })
        response.status_code = 201
        return response

    @mtp.route('/v1/meetups/<int:meetup_id>', methods = ['GET'])
    def get_meetup(meetup_id):
        meetup = MeetupInfo
        get_meetup = meetup.get_meetup(meetup_id)
        response = jsonify({
            'meetup':get_meetup
        })
        response.status_code = 200
        return response

    @mtp.route('/v1/get_meetups', methods = ['GET'])
    def get_meetups():
        meetup = MeetupInfo
        fetch_meetups = meetup.get_all_meetups()
        response = jsonify({
            'meetups':fetch_meetups
        })
        response.status_code = 200
        return response
