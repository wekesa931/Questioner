#import app.api.v1.views.user_views as app
import json
import unittest
from app import create_app

class TestApplication(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.users = {
                "firstname":"bill",
                "lastname":"wekesa",
                "othername":"adams",
                "email":"ill@wek",
                "phoneNumber":"526",
                "password":"tintinabulation"
            }
        self.meetups = {
                "createdOn":"12/12/2020",
                "location":"online",
                "images":"youtube.com/images",
                "topics":"javascript",
                "happeningOn":"12/12/2030",
                "tags":"classes"
            }
        self.questions = {
                "createdOn":'12/12/2020',
                "meetup":'javascript',
                "title":'lets learn',
                "body":'what is js',
                "votes":'20'
            }
    def tearDown(self):
        self.app.testing = False
        self.app = None

    def test_add_user_successful(self):
        response = self.client.post('/api/v1/user/auth/signup', json=self.users, content_type='application/json')
        self.assertIn('bill', response.data)
        self.assertEqual(response.status_code, 201)

    def test_add_meetup_successful(self):
        response = self.client.post('/api/v1/add_meetups', json=self.meetups, content_type='application/json')
        self.assertIn('online', response.data)
        self.assertEqual(response.status_code, 201)

    def test_get_meetups_sucessful(self):
        response = self.client.get('/api/v1/get_meetups')
        self.assertIn('online', response.data)
        self.assertEqual(response.status_code, 200)
    
    def test_get_specific_meetup_sucessful(self):
        response = self.client.get('/api/v1/meetups/1')
        self.assertIn('online', response.data)
        self.assertEqual(response.status_code, 200)

    def test_add_question_successful(self):
        response = self.client.post('/api/v1/post_question', json=self.questions, content_type='application/json')
        self.assertIn('javascript', response.data)
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()