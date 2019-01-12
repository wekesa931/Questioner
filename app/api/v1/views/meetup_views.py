from flask import Blueprint, Flask, jsonify, request, redirect
from app.api.v1.models.meetup_models import MeetupInfo
from app.validators.user_validators import Validators

validate = Validators()

mtp = Blueprint('meetup_api', __name__)

class MeetupViews:
    @mtp.route('/v1/add_meetups', methods = ['POST'])
    def create_meetup():
        meetup = request.get_json("meetups")
        if not meetup:
            return jsonify({"message":"No data found"}), 400
        if not all(val in meetup for val in [
                                "location",
                                "images", 
                                "topics", 
                                "happeningOn",
                                "tags",]):
            return jsonify({"message":"Some fields are missing"}), 400
            
        location = meetup['location']
        images = meetup['images']
        topics = meetup['topics']
        happeningOn = meetup['happeningOn']
        tags = meetup['tags']
        
        meetup_object = MeetupInfo(
                            '',
                            location,
                            topics,
                            happeningOn,
                            tags,
                            images
                            )
        meetups = meetup_object.add_meetup()
        return jsonify({
            'meetups':meetups
        }), 201

    @mtp.route('/v1/meetups/<int:meetup_id>', methods = ['GET'])
    def get_meetup(meetup_id):
        meetup = MeetupInfo
        get_meetup = meetup.get_meetup(meetup_id)
        if get_meetup == {}:
            return jsonify({
                "message":"meetup not found"
            }), 404
        response = jsonify({
            'meetup':get_meetup
        })
        response.status_code = 200
        return response

    @mtp.route('/v1/get_meetups', methods = ['GET'])
    def get_meetups():
        meetup = MeetupInfo
        fetch_meetups = meetup.get_all_meetups()
        if len(fetch_meetups) == 0:
            return jsonify({
                "message":"no meetups found"
            }), 404
        response = jsonify({
            'meetups':fetch_meetups
        })
        response.status_code = 200
        return response
