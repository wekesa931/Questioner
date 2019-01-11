from flask import Blueprint, Flask, jsonify
from app.api.v1.models.meetup_models import Reservation

rsv = Blueprint('rsv_api', __name__)

class GetReservation:
    @rsv.route('/v1/<int:meetup_id>/attend', methods = ['GET'])
    def attend_meetup(meetup_id):
        attendance = Reservation(meetup_id)
        confirmed = attendance.attend_meetup()
        response = jsonify({
            'meetup':confirmed
        })
        response.status_code = 200
        return response

    @rsv.route('/v1/<int:meetup_id>/reject', methods = ['GET'])
    def reject_meetup(meetup_id):
        attendance = Reservation(meetup_id)
        reject = attendance.reject_meetup()
        response = jsonify({
            'meetup':reject
        })
        response.status_code = 200
        return response

    @rsv.route('/v1/<int:meetup_id>/confirm', methods = ['GET'])
    def confirm_meetup(meetup_id):
        attendance = Reservation(meetup_id)
        confirm = attendance.not_certain()
        response = jsonify({
            'meetup':confirm
        })
        response.status_code = 200
        return response

