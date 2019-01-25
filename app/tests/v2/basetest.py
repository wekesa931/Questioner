import json
import unittest #this is a unit testing framework
from app import create_app
from app.api.v2.database.db_migrations import db

class TestApplication(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        #set up the test client
        self.client = self.app.test_client()
        """ set up user information test data """
        self.super_user = {
                "username":"wekesabill",
                "password":"Tintinabu@12"
        }

        self.users = {
                "firstname":"bill",
                "lastname":"wekesa",
                "othername":"adams",
                "username":"wekebill",
                "email":"ill@wek.com",
                "phoneNumber":"526",
                "password":"TIntinabu12@"
            }
        self.users_register = {
                "firstname":"john",
                "lastname":"terense",
                "othername":"dodo",
                "username":"teredo",
                "email":"terense@wek.com",
                "phoneNumber":"5246",
                "password":"TIntinabu12@"
            }
        
        self.users_two = {
                "firstname":"bill",
                "lastname":"wekesa",
                "othername":"adams",
                "username":"wekebill",
                "email":"ill@wek.com",
                "phoneNumber":"526",
                "password":"TIntinabu12@"
        }
        self.users_three = {
                "firstname":"bill",
                "lastname":"wekesa",
                "othername":"adams",
                "username":"wekesadamsbill",
                "email":"ill@wek.com",
                "phoneNumber":"5236",
                "password":"TIntinabu12@"
        }
        self.users_four = {
                "firstname":"bill",
                "lastname":"wekesa",
                "othername":"adams",
                "username":"wekbill",
                "email":"il@wek.com",
                "phoneNumber":"526",
                "password":"TIntin"
        }
        self.users_five = {
                "firstname":"bill",
                "lastname":"wekesa",
                "othername":"adams",
                "username":"wekbill",
                "email":"ilwek.com",
                "phoneNumber":"526",
                "password":"TIntinabu12@"
        }

        """ set up meetup information test data """
        self.meetups = {
                "location":"online",
                "images":"youtube.com",
                "topic":"javascript",
                "happeningOn":"2030-10-10",
                "tags":"classes"
            }
        self.meetups_one = {
                "location":"",
                "images":"youtube.com/images",
                "topic":"javascript",
                "happeningOn":"12/12/2030",
                "tags":"classes"
            }
        self.meetups_two = {
                "images":"youtube.com/images",
                "topic":"javascript",
                "happeningOn":"12/12/2030",
                "tags":"classes"
            }
        self.reservation = { 
                "status":"YES"
        }
        self.comment = {
                "comment":"welcome to the world"
        }
        self.image = {
                "image":"image.com"
        }
        self.image_one = {
                "image":""
        }
        self.tags = {
                "tags":"my tag"
        }
        self.tag_one = {
                "tags":""
        }

        """ set up questions information test data """
        self.questions = {
                "title":"adams",
                "body":"ill@wek"
            }
        self.question_one = {
                "title":"",
                "body":"ill@wek"
        }
        self.question_two = {
                "body":"ill@wek"
        }
        self.vote = {
                "body": "ill@wek",
                "question": 1,
                "title": "adams",
                "votes": 1
            }

    def tearDown(self):
        """ Pull down data to original after testing """
        db.drop_tables()
        self.app.testing = False
        self.app = None

    if __name__ == '__main__':
            unittest.main()