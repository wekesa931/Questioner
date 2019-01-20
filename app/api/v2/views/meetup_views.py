from flask import Blueprint, Flask, jsonify, request
from app.api.v2.models.user_models import UserInfo
from app.api.v2.models.images_models import AddImage
from app.api.v2.models.tags_models import AddTags
from app.api.v2.models.meetup_models import MeetupInfo
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
        check_admin = UserInfo.get_admin(user_id)
        if check_admin == False:
            return jsonify({
                'status': 403,
                'message': 'Permission denied!'
            }), 403
        meetup = request.get_json("meetups")
        validate_info = ['location','images','topic',
                                'happeningOn','tags']
        error = check_fields(meetup, validate_info)
        if len(error) > 0:
            return jsonify({
                "status": 400,
                "message":error
            }), 400
            
        location = meetup['location']
        images = meetup['images']
        topic = meetup['topic']
        happeningOn = meetup['happeningOn']
        tags = meetup['tags']
        meetup_object = MeetupInfo(location,topic,happeningOn,
                                            tags,images)
        meetups = meetup_object.add_meetup()
        return jsonify({
            'status': 201,
            'data':[{
                'meetups':meetups
            }]
        }), 201

    @mtp_two.route('/v2/meetups/<int:meetup_id>', methods = ['GET'])
    @token_required
    def get_meetup(user_id, meetup_id):
        """ Gets  specific meetup id """
        images = AddImage.single_image(meetup_id)
        tags = AddTags.single_tag(meetup_id)
        all_meetups = MeetupInfo.get_meetups()
        for meetup in all_meetups:            
            if meetup['id'] == meetup_id:
                return jsonify({
                    'status': 200,
                    'data':[{
                        'meetup':meetup,
                        'images':images,
                        'tags':tags
                    }]
                }), 200
        return jsonify({
            "status": 404,
            "message":"meetup not found"
        }), 404

    @mtp_two.route('/v2/get_meetups', methods = ['GET'])
    @token_required
    def get_meetups(user_id):
        """ gets all meetups """
        all_meetups = MeetupInfo.get_meetups()
        if len(all_meetups) == 0:
            return jsonify({"message":"no meetups found"}), 404
        return jsonify({
            'status': 200,
            'data':[{
                'meetup':all_meetups
            }]
        }), 200

    @mtp_two.route('/v2/meetups/<int:meetup_id>/delete', methods = ['DELETE'])
    @token_required
    def del_meetup(user_id, meetup_id):
        """ Gets  specific meetup id """
        check_admin = UserInfo.get_admin(user_id)
        if check_admin == False:
            return jsonify({
                'status': 403,
                'message': 'Permission denied!'
            }), 403
        user = UserInfo.get_one_user(user_id)
        all_meetups = MeetupInfo.get_meetups()
        print(meetup_id)
        for meetup in all_meetups:            
            if meetup['id'] == meetup_id:
                remove_meetup = MeetupInfo.del_meetup(meetup_id)
                print(remove_meetup)
                return jsonify({
                        'status': 200,
                        'data':[{
                            'message':'meetup deleted successfully!'
                        }]
                }), 200        
        return jsonify({
            "status": 400,
            "message":"meetup not found"
        }), 404
        