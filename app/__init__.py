from flask import Flask

def create_app():
    app = Flask(__name__)
    from app.api.v1.views.user_views import mod
    app.register_blueprint(api.v1.views.user_views.mod, url_prefix='/api')
    return app