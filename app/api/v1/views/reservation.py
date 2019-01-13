from flask import Blueprint, Flask, jsonify, request
from app.api.v1.models.reservation_models import Reservation
from app.api.v1.models.meetup_models import MeetupInfo

rsv = Blueprint('rsv_api', __name__)

class GetReservation:
    @rsv.route('/v1/<int:meetup_id>/attend', methods = ['POST'])
    def attend_meetup(meetup_id):

        meetup = MeetupInfo
        get_meetup = meetup.get_meetup(meetup_id) 
        if get_meetup == {}:
            return jsonify({
                "message":"meetup not found"
            }), 404

        attendance = request.get_json("rsvp")
        topic = attendance["topic"]
        status = attendance["status"]

        if not all(val in attendance for val in [
                                "topic",
                                "status"]):
            return jsonify({"message":"Some fields are missing"}), 400

        confirmed = Reservation(
                            meetup_id,
                            topic,
                            status
                        )
        rsvp = confirmed.meetup_status()
        response = jsonify({
            'Reservation':rsvp
        })
        response.status_code = 200
        return response