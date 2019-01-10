from flask import Flask
from config import app_config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    
    from app.api.v1.views.user_views import mod
    app.register_blueprint(api.v1.views.user_views.mod, url_prefix='/api')
    
    return app