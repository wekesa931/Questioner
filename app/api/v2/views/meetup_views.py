from flask import Blueprint, Flask, jsonify, request
from app.api.v2.models.user_models import UserInfo
from app.api.v2.models.images_models import AddImage
from app.api.v2.models.tags_models import AddTags
from app.api.v2.models.meetup_models import MeetupInfo
from app.validators.shared_validators import check_fields
from app.validators.user_validators import Validators
from app.validators.token_validation import token_required
from app.validators.repeat_validation import check_valid

validate = Validators()

#set up meetup views blueprints
mtp_two = Blueprint('meetup_api', __name__)

class MeetupViews:
    """ Defines the meetup route """
    @mtp_two.route('/v2/meetups', methods = ['POST'])
    @token_required
    def create_meetup(is_admin,user_id):
        """ fetch the posted information from the user """
        if not is_admin:
            return jsonify({
                'status': 403,
                'error': 'Permission denied!'
            }), 403
        meetup = request.get_json("meetups")
        validate_info = ['location','images','topic',
                                'happeningOn','tags']
        error = check_fields(meetup, validate_info)
        if len(error) > 0:
            return jsonify({"status": 400,"message":error}), 400
        location = meetup['location']
        images = meetup['images']
        topic = meetup['topic']
        happeningOn = meetup['happeningOn']
        if not validate.check_date(happeningOn):
            return jsonify({'status': 400,"message":"date should be in the format yyyy-mm-dd"}), 400
        tags = meetup['tags']
        meetup_validation = check_valid(location,topic,happeningOn)
        if len(meetup_validation) > 0:
            return jsonify({
                "status": 400,
                "message":meetup_validation
            }), 400
        meetup_object = MeetupInfo(user_id,location,topic,happeningOn,
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
    def get_meetup(user_id,is_admin, meetup_id):
        """ Gets  specific meetup id """
        images = AddImage.single_image(meetup_id)
        tags = AddTags.single_tag(meetup_id)
        current_meetup = MeetupInfo.get_one_meetup(meetup_id)         
        if current_meetup:
            images.append(current_meetup['images'])
            tags.append(current_meetup['tags'])
            return jsonify({
                'status': 200,
                'data':[{
                    'meetup':{
                        'Date created':current_meetup['createdon'],
                        'Date happening':current_meetup['happeningon'],
                        'Images':images,
                        'Location':current_meetup['location'],
                        'Tags':tags,
                        'Meetup topic':current_meetup['topic']
                        }
                }]
            }), 200
        return jsonify({
            "status": 404,
            "error":"meetup not found"
        }), 404

    @mtp_two.route('/v2/meetups', methods = ['GET'])
    @token_required
    def get_meetups(user_id,is_admin):
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

    @mtp_two.route('/v2/meetups/<int:meetup_id>', methods = ['DELETE'])
    @token_required
    def del_meetup(user_id,is_admin,meetup_id):
        """ Gets  specific meetup id """
        if is_admin == False:
            return jsonify({
                'status': 403,
                'message': 'Permission denied!'
            }), 403
        current_meetup = MeetupInfo.get_one_meetup(meetup_id)         
        if current_meetup:           
            MeetupInfo.del_meetup(meetup_id)
            return jsonify({
                    'status': 200,
                    'data':[{
                        'message':'meetup deleted successfully!'
                    }]
            }), 200        
        return jsonify({
            "status": 400,
            "error":"meetup not found"
        }), 404
        