from flask import Blueprint, Flask, jsonify, request
from app.api.v2.models.tags_models import AddTags
from app.api.v2.models.user_models import UserInfo
from app.api.v2.models.meetup_models import MeetupInfo
from app.validators.shared_validators import check_fields
from app.validators.token_validation import token_required

tgs_two = Blueprint('tags_api', __name__)

class TagsViews:
    """ Defines the meetup route """
    @tgs_two.route('/v2/meetup/<int:meetup_id>/tags', methods = ['POST'])
    @token_required
    def add_tags(user_id,is_admin,meetup_id):
        """ fetch the posted information from the user """
        if is_admin == False:
            return jsonify({
                'status': 403,
                'error': 'Permission denied!'
            }), 403
        tags = request.get_json("tags")
        validate_info = ['tags']
        error = check_fields(tags, validate_info)
        if len(error) > 0:
            return jsonify({
                "status": 400,
                "error":error
            }), 400
        all_meetups = MeetupInfo.get_meetups()
        for meetup in all_meetups:
            if meetup['id'] == meetup_id:
                tag_item = tags['tags']
                topic = meetup['topic']
                tags_object = AddTags(meetup_id,topic,tag_item)
                all_tags = tags_object.add_tags()
                return jsonify({
                    'status': 201,
                    'data':[{
                        'tags':all_tags
                    }]
                }), 201
        return jsonify({
            "status": 400,
            "error":'meetup {} not found'.format(meetup_id)
        }), 400