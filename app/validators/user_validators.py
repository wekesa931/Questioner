import re
from app.api.v1.models.user_models import users

class Validators():
    def check_password(self, password):
        """ Minimum eight characters, at least one letter and one number """
        return re.match('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password)

    def check_email(self, email):
        return re.match('[^@]+@[^@]+\.[^@]+',email) 

    def check_repeated(self, username):
        for key_item, value_item in users.items():
            for dict_key, dict_value in value_item.items():
                if dict_value == username:
                    return True
        return False
    def check_username(self):
        pass