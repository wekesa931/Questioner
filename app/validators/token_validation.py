from flask import current_app
from functools import wraps
from flask import request, jsonify
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', None)

        if token == None:
            return jsonify({
                'status': 403,
                'message':'Token is missing!'
            }), 403
        else:
            try:
                token = token.split("Bearer ")
                token = token[1]
                secret=current_app.config['SECRET']
                data = jwt.decode(token, secret)
                print(data)
                user_id = data['user_id']
                is_admin = data['isadmin']
                print(is_admin)
            except:
                return jsonify({
                    'status': 403,
                    'message':'Token is invalid'
                }), 403
            return f(user_id=user_id, is_admin=is_admin, *args, **kwargs)
    return decorated
    