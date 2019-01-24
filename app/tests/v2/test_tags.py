from app.tests.v2.basetest import TestApplication
import json

class TestTags(TestApplication):
    """ test the questions endpoints """
    
    def test_add_tags_successful(self):
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
            '/api/v2/meetup/1/tags',
            headers = dict(Authorization = "Bearer " + token),
            json=self.tags, 
            content_type='application/json'
            )
        self.assertIn(u'my tag', response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_add_tags_failure(self):
        """ test if question is successfuly added """
        tags={}
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
            '/api/v2/meetup/1/tags',
            headers = dict(Authorization = "Bearer " + token),
            json=tags, 
            content_type='application/json'
            )
        self.assertIn(u'No data found', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_add_tags_field_absent(self):
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
            '/api/v2/meetup/1/tags',
            headers = dict(Authorization = "Bearer " + token),
            json=self.tag_one, 
            content_type='application/json'
            )
        self.assertIn(u'tags is missing a value', response.data.decode())
        self.assertEqual(response.status_code, 400)