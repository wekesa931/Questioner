from flask import Blueprint, Flask, jsonify, request
from app.api.v2.models.images_models import AddImage
from app.api.v2.models.user_models import UserInfo
from app.api.v2.models.meetup_models import MeetupInfo
from app.validators.user_validators import Validators
from app.validators.shared_validators import check_fields
from app.validators.token_validation import token_required

validate = Validators()

imgs_two = Blueprint('imagestags_api', __name__)

class ImageViews:
    """ Defines the meetup route """
    @imgs_two.route('/v2/meetup/<int:meetup_id>/image', methods = ['POST'])
    @token_required
    def add_image(user_id,meetup_id,is_admin):
        """ fetch the posted information from the user """
        if not is_admin:
            return jsonify({
                'status': 403,
                'error': 'Permission denied!'
            }), 403
        image = request.get_json("image")
        validate_info = ['image']
        error = check_fields(image, validate_info)
        if len(error) > 0:
            return jsonify({
                "status": 400,
                "error":error
            }), 400
        if not validate.check_url(image['image']):
            return jsonify({
                'status': 400,
                "error":"URL is not valid"
            }), 400
        meetup = MeetupInfo.get_one_meetup(meetup_id)
        if meetup:
            image_item = image['image']
            topic = meetup['topic']
            image_object = AddImage(meetup_id,topic,image_item)
            add_image_item = image_object.add_image()
            return jsonify({
                'status': 201,
                'data':[{
                    'image':add_image_item
                }]
            }), 201
        return jsonify({
            "status": 400,
            "error":'meetup {} not found'.format(meetup_id)
        }), 400