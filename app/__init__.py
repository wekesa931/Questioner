from flask import Flask
from config import app_config
from app.api.v2.database.db_migrations import db

def create_app(config_name):
    """ create the flask instance """
    app = Flask(__name__)
    """ Enable us use the defined configurations in config file """
    app.config.from_object(app_config[config_name])
    
    """ Import the blueprints from views files """
    #from app.api.v1.views.user_views import mod
    #from app.api.v1.views.meetup_views import mtp
    #from app.api.v1.views.question_views import qsn
    #from app.api.v1.views.reservation import rsv
    #from app.api.v1.views.vote import vt

    """ register verson two blueprints """
    from app.api.v2.views.user_views import mod_two
    from app.api.v2.views.meetup_views import mtp_two
    from app.api.v2.views.question_views import qsn_two
    from app.api.v2.views.reservation import rsv_two
    from app.api.v2.views.vote import vt_two



    """ register the blueprints """
    #app.register_blueprint(api.v1.views.user_views.mod, url_prefix='/api')
    #app.register_blueprint(api.v1.views.meetup_views.mtp, url_prefix='/api')
    #app.register_blueprint(api.v1.views.question_views.qsn, url_prefix='/api')
    #app.register_blueprint(api.v1.views.reservation.rsv, url_prefix='/api')
    #app.register_blueprint(api.v1.views.vote.vt, url_prefix='/api') 

    """ register v2 blueprints """
    app.register_blueprint(api.v2.views.user_views.mod_two, url_prefix='/api')
    app.register_blueprint(api.v2.views.meetup_views.mtp_two, url_prefix='/api')
    app.register_blueprint(api.v2.views.question_views.qsn_two, url_prefix='/api')
    app.register_blueprint(api.v2.views.reservation.rsv_two, url_prefix='/api')
    app.register_blueprint(api.v2.views.vote.vt_two, url_prefix='/api') 

    configure_extensions()
    
    return app

def configure_extensions():
    db.migrations()