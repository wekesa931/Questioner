from flask import Blueprint

mod = Blueprint('api', __name__)

@mod.route('/')
def getStuff():
    return '{"results":"you are in the yeeees"}'