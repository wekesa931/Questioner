from flask import Blueprint

mod = Blueprint('api', __name__)

@mod.route('/getStuff')
def getStuff():
    return '{"results":"you are in the yeeees"}'