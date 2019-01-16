import re
from app.api.v1.models.user_models import users

class Validators():
    """ Validates user information on regisration """
    def check_password(self, password):
        """ Minimum eight characters, at least one letter and one number """
        return re.match('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password)

    def check_email(self, email):
        """ must have @ special character """
        return re.match('[^@]+@[^@]+\.[^@]+',email) 

    def check_repeated(self, username):
        """ Checks for repeated username """
        for key_item, value_item in users.items():
            for dict_key, dict_value in value_item.items():
                if dict_value == username:
                    return True
        return False