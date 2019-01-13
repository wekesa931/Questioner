from flask import Blueprint, Flask, jsonify, request, redirect
from app.api.v1.models.meetup_models import MeetupInfo
from app.validators.shared_validators import check_fields

mtp = Blueprint('meetup_api', __name__)

class MeetupViews:
    @mtp.route('/v1/add_meetups', methods = ['POST'])
    def create_meetup():
        meetup = request.get_json("meetups")
        validate_info = ['location','images','topic',
                                'happeningOn','tags']
        error = check_fields(meetup, validate_info)
        if len(error) > 0:
            return jsonify({"message":error}), 400
            
        location = meetup['location']
        images = meetup['images']
        topic = meetup['topic']
        happeningOn = meetup['happeningOn']
        tags = meetup['tags']
        meetup_object = MeetupInfo('',location,topic,happeningOn,
                                            tags,images)
        meetups = meetup_object.add_meetup()
        return jsonify({
            'status': '201',
            'data':[{
                'meetups':meetups
            }]
        }), 201

    @mtp.route('/v1/meetups/<int:meetup_id>', methods = ['GET'])
    def get_meetup(meetup_id):
        meetup = MeetupInfo
        get_meetup = meetup.get_meetup(meetup_id)
        if get_meetup == {}:
            return jsonify({
                "message":"meetup not found"
            }), 404
        return jsonify({
            'status': '200',
            'data':[{
                'meetup':get_meetup
            }]
       }), 200

    @mtp.route('/v1/get_meetups', methods = ['GET'])
    def get_meetups():
        meetup = MeetupInfo
        fetch_meetups = meetup.get_all_meetups()
        if len(fetch_meetups) == 0:
            return jsonify({"message":"no meetups found"}), 404

        return jsonify({
            'status': '200',
            'data':[{
                'meetup':fetch_meetups
            }]
       }), 200