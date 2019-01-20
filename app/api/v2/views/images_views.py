from flask import Blueprint, Flask, jsonify, request
from app.api.v2.models.images_models import AddImage
from app.api.v2.models.meetup_models import MeetupInfo
from app.validators.shared_validators import check_fields
from app.validators.token_validation import token_required

imgs_two = Blueprint('imagestags_api', __name__)

class ImageViews:
    """ Defines the meetup route """
    @imgs_two.route('/v2/meetup/<int:meetup_id>/image', methods = ['POST'])
    @token_required
    def add_image(user_id,meetup_id):
        """ fetch the posted information from the user """
        image = request.get_json("image")
        validate_info = ['image']
        error = check_fields(image, validate_info)
        if len(error) > 0:
            return jsonify({
                "status": 400,
                "message":error
            }), 400
        all_meetups = MeetupInfo.get_meetups()
        for meetup in all_meetups:
            if meetup['id'] == meetup_id:
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
            "message":'meetup {} not found'.format(meetup_id)
        }), 400