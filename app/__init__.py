from flask import Flask

app = Flask(__name__)

from app.api.v1.views.routes import mod

app.register_blueprint(api.v1.views.routes.mod, url_prefix='/api')