from app.tests.v2.basetest import TestApplication
import json

class TestImage(TestApplication):
    """ test the questions endpoints """
    
    def test_add_image_successful(self):
        """ test if question is successfuly added """
        self.client.post('/api/v2/user/auth/signup', json=self.users, content_type='application/json')
        results = self.client.post('/api/v2/user/auth/login', json=self.users, content_type='application/json')
        token = json.loads(results.data.decode())['data'][0]['token']
        self.client.post(
            '/api/v2/meetups',
            headers = dict(Authorization = "Bearer " + token),
            json=self.meetups,
            content_type='application/json'
            )
        
        response = self.client.post(
            '/api/v2/meetup/1/image',
            headers = dict(Authorization = "Bearer " + token),
            json=self.image, 
            content_type='application/json'
            )
        self.assertIn(u'my awesome image', response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_add_image_failure(self):
        """ test if question is successfuly added """
        image={}
        self.client.post('/api/v2/user/auth/signup', json=self.users, content_type='application/json')
        results = self.client.post('/api/v2/user/auth/login', json=self.users, content_type='application/json')
        token = json.loads(results.data.decode())['data'][0]['token']
        self.client.post(
            '/api/v2/meetups',
            headers = dict(Authorization = "Bearer " + token),
            json=self.meetups,
            content_type='application/json'
            )
        response = self.client.post(
            '/api/v2/meetup/1/image',
            headers = dict(Authorization = "Bearer " + token),
            json=image, 
            content_type='application/json'
            )
        self.assertIn(u'No data found', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_add_image_field_absent(self):
        """ test if question is successfuly added """
        self.client.post('/api/v2/user/auth/signup', json=self.users, content_type='application/json')
        results = self.client.post('/api/v2/user/auth/login', json=self.users, content_type='application/json')
        token = json.loads(results.data.decode())['data'][0]['token']
        self.client.post(
            '/api/v2/meetups',
            headers = dict(Authorization = "Bearer " + token),
            json=self.meetups,
            content_type='application/json'
            )
        response = self.client.post(
            '/api/v2/meetup/1/image',
            headers = dict(Authorization = "Bearer " + token),
            json=self.image_one, 
            content_type='application/json'
            )
        self.assertIn(u'image is missing a value', response.data.decode())
        self.assertEqual(response.status_code, 400)