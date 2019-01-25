from flask import Blueprint, Flask, jsonify, request
from app.api.v2.models.reservation_models import Reservation
from app.api.v2.models.meetup_models import MeetupInfo
from app.validators.shared_validators import check_fields
from app.validators.token_validation import token_required

#set up reservation views blueprints
rsv_two = Blueprint('rsv_api', __name__)

class GetReservation:
    """ Defines the meeup route """
    @rsv_two.route('/v2/<int:meetup_id>/rsvp', methods = ['POST'])
    @token_required
    def attend_meetup(user_id,is_admin, meetup_id):
        all_meetups = MeetupInfo.get_meetups()
        for meetup in all_meetups:
            if meetup['id'] == meetup_id:
                attendance = request.get_json("rsvp")
                validate_info = ['status']
                error = check_fields(attendance, validate_info)
                if len(error) > 0:
                    return jsonify({
                        'status':400,
                        "message":error
                        }), 400
                topic = meetup["topic"]
                status = attendance["status"]
                confirmed = Reservation(user_id, meetup_id, topic, status)
                rsvp = confirmed.make_reservation()
                return jsonify({
                    'status':200,
                    'data':[{'Reservation':rsvp}]
                }), 200
       
        return jsonify({
            'status': 404,
            "error": "no meetup found"
        }), 404

    @rsv_two.route('/v2/rsvp', methods = ['GET'])
    @token_required
    def get_reservations(user_id,is_admin):
        """ gets all reservations """
        all_meetups = MeetupInfo.get_meetups()   
        all_reservations = []  
        if all_meetups:
            my_rsvp = Reservation.attendance()
            if len(my_rsvp) > 0:
                for meetup in all_meetups:
                    for rsvp in my_rsvp:
                        if rsvp['meetup_id'] == meetup['id']:
                            all_reservations.append(meetup)
                return jsonify({'status': 200,"data":[{'reservations':all_reservations}]}), 200

            return jsonify({'status': 404,"error":"no reservations made"}), 404

        return jsonify({'status': 404,"error":"no meetups found"}), 404