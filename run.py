""" os provides a way of using functionalities dependent on the operating sysytem """
import os
from app import create_app

""" Return the value of the environment variable """
config_name = os.getenv('flask_config')

""" Environment variables are sent to create_app and gets configurations to run the app """
app = create_app('development')

if __name__ == '__main__':
    app.run()
