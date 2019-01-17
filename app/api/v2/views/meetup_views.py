from flask import Blueprint, Flask, jsonify, request
from app.api.v1.models.meetup_models import MeetupInfo
from app.validators.shared_validators import check_fields
from app.validators.token_validation import token_required

#set up meetup views blueprints
mtp_two = Blueprint('meetup_api', __name__)

class MeetupViews:
    """ Defines the meetup route """
    @mtp_two.route('/v2/add_meetups', methods = ['POST'])
    @token_required
    def create_meetup(user_id):
        """ fetch the posted information from the user """
        meetup = request.get_json("meetups")
        print(user_id)
        #validate user information
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
        #Meetup information is sent to database
        meetup_object = MeetupInfo('',location,topic,happeningOn,
                                            tags,images)
        meetups = meetup_object.add_meetup()
        return jsonify({
            'status': '201',
            'data':[{
                'meetups':meetups
            }]
        }), 201

    @mtp_two.route('/v2/meetups/<int:meetup_id>', methods = ['GET'])
    @token_required
    def get_meetup(user_id, meetup_id):
        """ Gets  specific meetup id """
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

    @mtp_two.route('/v2/get_meetups', methods = ['GET'])
    @token_required
    def get_meetups(user_id):
        """ gets all meetups """
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