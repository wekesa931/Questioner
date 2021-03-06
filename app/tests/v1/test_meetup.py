from app.tests.v1.basetest import TestApplication
import json

class TestMeetup(TestApplication):
    """ test the meetup endpoints"""
    def test_add_meetup_successful(self):
        """ test if meetups are added successfuly """
        self.client.post('/api/v1/user/auth/signup', json=self.users, content_type='application/json')
        results = self.client.post('/api/v1/user/auth/login', json=self.users, content_type='application/json')
        token = json.loads(results.data.decode())['token']
        response = self.client.post(
            '/api/v1/add_meetups',
            headers = dict(Authorization="Bearer " + token),
            json=self.meetups, 
            content_type='application/json'
            )
        self.assertIn(u'online', response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_add_meetup_failure(self):
        """ test if meetups addition fail """
        meetups = {}

        self.client.post('/api/v1/user/auth/signup', json=self.users, content_type='application/json')
        results = self.client.post('/api/v1/user/auth/login', json=self.users, content_type='application/json')
        token = json.loads(results.data.decode())['token']
        response = self.client.post(
            '/api/v1/add_meetups',
            headers = dict(Authorization="Bearer " + token),
            json=meetups, 
            content_type='application/json'
            )
        self.assertIn(u'No data found', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_get_meetups_sucessful(self):     
        """ test if meetups are returned on call """   
        self.client.post('/api/v1/user/auth/signup', json=self.users, content_type='application/json')
        results = self.client.post('/api/v1/user/auth/login', json=self.users, content_type='application/json')
        token = json.loads(results.data.decode())['token']
        response = self.client.get(
            '/api/v1/get_meetups',
            headers = dict(Authorization="Bearer " + token))
        self.assertIn(u'online', response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_get_meetup_failure(self):
        """ confirms the status response on failure """
        meetups = {}
        self.client.post('/api/v1/user/auth/signup', json=self.users, content_type='application/json')
        results = self.client.post('/api/v1/user/auth/login', json=self.users, content_type='application/json')
        token = json.loads(results.data.decode())['token']
        self.client.post('/api/v1/add_meetups', json=self.meetups, 
            content_type='application/json'
            )
        response = self.client.get('/api/v1/meetups/1',
            headers = dict(Authorization="Bearer " + token),
             json=meetups, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_create_reservation(self):
        """ test if reservatios are created """

        self.client.post('/api/v1/user/auth/signup', json=self.users, content_type='application/json')
        results = self.client.post('/api/v1/user/auth/login', json=self.users, content_type='application/json')
        token = json.loads(results.data.decode())['token']
        response = self.client.post(
            '/api/v1/1/attend',
            headers = dict(Authorization="Bearer " + token),
            json=self.reservation, content_type='application/json')
        self.assertIn(u'YES', response.data.decode())
        self.assertEqual(response.status_code, 200)
    
    def test_get_specific_meetup_sucessful(self):
        """ test if specific meetup can be obtained """
        self.client.post('/api/v1/user/auth/signup', json=self.users, content_type='application/json')
        results = self.client.post('/api/v1/user/auth/login', json=self.users, content_type='application/json')
        token = json.loads(results.data.decode())['token']
        response = self.client.get('/api/v1/meetups/1',
            headers = dict(Authorization="Bearer " + token))
        self.assertIn(u'online', response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_if_meetup_data_available(self):
        """ test if meetup fields are available """
        self.client.post('/api/v1/user/auth/signup', json=self.users, content_type='application/json')
        results = self.client.post('/api/v1/user/auth/login', json=self.users, content_type='application/json')
        token = json.loads(results.data.decode())['token']
        response = self.client.post(
            '/api/v1/add_meetups',
            headers = dict(Authorization="Bearer " + token),
            json=self.meetups_one, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(u'location is missing', response.data.decode())

    def test_if_meetup_field_available(self):
        """ test if meetup data is available """
        self.client.post('/api/v1/user/auth/signup', json=self.users, content_type='application/json')
        results = self.client.post('/api/v1/user/auth/login', json=self.users, content_type='application/json')
        token = json.loads(results.data.decode())['token']
        response = self.client.post(
            '/api/v1/add_meetups',
            headers = dict(Authorization="Bearer " + token),
            json=self.meetups_two, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(u'location is missing', response.data.decode())