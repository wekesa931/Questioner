import re
from app.api.v2.models.user_models import UserInfo


class Validators():
    """ Validates user information on regisration """
    def check_password(self, password):
        """ Minimum eight characters, at least one letter and one number """
        return re.match('^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', password)

    def check_email(self, email):
        """ must have @ special character """
        return re.match('[^@]+@[^@]+\.[^@]+',email) 

    def check_repeated(self, item):
        """ Checks for repeated username """
        all_users = UserInfo.get_all_users()
        for user in all_users:
            for dict_key, dict_value in user.items():
                if dict_value == item:
                    return True
        return False
    def check_date(self,happeningOn):
        return re.match('^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$',happeningOn) 
        