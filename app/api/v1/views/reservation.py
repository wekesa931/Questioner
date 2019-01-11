from flask import Blueprint, Flask, jsonify, request
from app.api.v1.models.meetup_models import Reservation

rsv = Blueprint('rsv_api', __name__)

class GetReservation:
    @rsv.route('/v1/<int:meetup_id>/attend', methods = ['POST'])
    def attend_meetup(meetup_id):
        attendance = request.get_json("rsvp")
        topic = attendance["topic"]
        status = attendance["status"]
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