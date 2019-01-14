from flask import Flask
from config import app_config

def create_app(config_name):
    """ create the flask instance """
    app = Flask(__name__)
    """ Enable us use the defined configurations in config file """
    app.config.from_object(app_config[config_name])
    
    """ Import the blueprints from views files """
    from app.api.v1.views.user_views import mod
    from app.api.v1.views.meetup_views import mtp
    from app.api.v1.views.question_views import qsn
    from app.api.v1.views.reservation import rsv
    from app.api.v1.views.vote import vt

    """ register the blueprints """
    app.register_blueprint(api.v1.views.user_views.mod, url_prefix='/api')
    app.register_blueprint(api.v1.views.meetup_views.mtp, url_prefix='/api')
    app.register_blueprint(api.v1.views.question_views.qsn, url_prefix='/api')
    app.register_blueprint(api.v1.views.reservation.rsv, url_prefix='/api')
    app.register_blueprint(api.v1.views.vote.vt, url_prefix='/api') 
    
    return app