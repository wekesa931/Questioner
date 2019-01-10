import app.api.v1.views.user_views as app
import json
import unittest

class TestApplication(unittest.TestCase):
    def setUp(self):
        self.client = test_client()

    def test_add_user(self):
        self.users = {
                "firstname":"bill",
                "lastname":"wekesa",
                "othername":"adams",
                "email":"ill@wek",
                "phoneNumber":"526",
                "password":"tintinabulation"
            }        
        app.user_signup.user_info = {
                "firstname":"bill",
                "lastname":"wekesa",
                "othername":"adams",
                "email":"ill@wek",
                "phoneNumber":"526",
                "password":"tintinabulation"
            }
        self.assertEqual(self.users, app.user_signup.user_info)
        self.assertEqual(respon.status_code, 400)
    def test_create_meetup(self):
        self.meetups = {
                "createdOn":"12/12/2020",
                "location":"online",
                "images":"youtube.com/images",
                "topics":"javascript",
                "happeningOn":"12/12/2030",
                "tags":"classes"
            }
        app.create_meetup.meetup = {
                "createdOn":"12/12/2020",
                "location":"online",
                "images":"youtube.com/images",
                "topics":"javascript",
                "happeningOn":"12/12/2030",
                "tags":"classes"
            }
        self.assertEqual(self.meetups, app.create_meetup.meetup)

    def test_createQuestion(self):
        pass

    def test_get_specific_meetup(self):
        pass

    def test_get_meetups(self):
        pass

    def test_upvote_question(self):
        pass
    
    def test_downvote_question(self):
        pass

    def test_rsvp_question(self):
        pass