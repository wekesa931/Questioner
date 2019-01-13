from flask import Blueprint, Flask, jsonify, request
from app.api.v1.models.reservation_models import Reservation
from app.api.v1.models.meetup_models import MeetupInfo
from app.validators.shared_validators import check_fields

#set up reservation views blueprints
rsv = Blueprint('rsv_api', __name__)

class GetReservation:
    """ Defines the meeup route """
    @rsv.route('/v1/<int:meetup_id>/attend', methods = ['POST'])
    def attend_meetup(meetup_id):
        meetup = MeetupInfo
        get_meetup = meetup.get_meetup(meetup_id) 
        #validate obtained information
        if get_meetup == {}:
            return jsonify({"message":"meetup not found"}), 404
        attendance = request.get_json("rsvp")
        validate_info = ['status']
        #validate obtained information
        error = check_fields(attendance, validate_info)
        if len(error) > 0:
            return jsonify({"message":error}), 400
        topic = get_meetup["topic"]
        status = attendance["status"]
        confirmed = Reservation(meetup_id,topic,status)
        rsvp = confirmed.meetup_status()
        return jsonify({'Reservation':rsvp}), 200