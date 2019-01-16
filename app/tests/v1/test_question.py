from app.tests.v1.basetest import TestApplication
import json

class TestQuestion(TestApplication):
    """ test the questions endpoints """
    
    def test_add_question_successful(self):
        """ test if question is successfuly added """
        self.client.post('/api/v1/user/auth/signup', json=self.users, content_type='application/json')
        results = self.client.post('/api/v1/user/auth/login', json=self.users, content_type='application/json')
        token = json.loads(results.data.decode())['token']
        self.client.post(
            '/api/v1/add_meetups',
            headers = dict(Authorization = "Bearer " + token),
            json=self.meetups,
            content_type='application/json'
            )
        
        response = self.client.post(
            '/api/v1/1/post_question',
            headers = dict(Authorization = "Bearer " + token),
            json=self.questions, 
            content_type='application/json'
            )
        self.assertIn(u'ill@wek', response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_add_question_failure(self):
        """ test if question fails validation """
        questions = {}
        self.client.post('/api/v1/user/auth/signup', json=self.users, content_type='application/json')
        results = self.client.post('/api/v1/user/auth/login', json=self.users, content_type='application/json')
        token = json.loads(results.data.decode())['token']
        self.client.post(
            '/api/v1/add_meetups',
            headers = dict(Authorization = "Bearer " + token),
            json=self.meetups,
            content_type='application/json'
            )

        response = self.client.post(
            '/api/v1/1/post_question',
            headers = dict(Authorization="Bearer " + token),
            json=questions,
            content_type='application/json'
            )
        self.assertIn(u'No data found', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_if_question_data_available(self):
        """ test if specific question id is existent """
        self.client.post('/api/v1/user/auth/signup', json=self.users, content_type='application/json')
        results = self.client.post('/api/v1/user/auth/login', json=self.users, content_type='application/json')
        token = json.loads(results.data.decode())['token']
        self.client.post(
            '/api/v1/add_meetups',
            headers = dict(Authorization = "Bearer " + token),
            json=self.meetups,
            content_type='application/json'
            )
        response = self.client.post(
            '/api/v1/1/post_question',
            headers = dict(Authorization="Bearer " + token),
            json=self.question_one, 
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 400)
        self.assertIn(u'title is missing a value', response.data.decode())

    def test_upvote(self):
        """ test the upvote api """
        self.client.post('/api/v1/user/auth/signup', json=self.users, content_type='application/json')
        results = self.client.post('/api/v1/user/auth/login', json=self.users, content_type='application/json')
        token = json.loads(results.data.decode())['token']
        self.client.post(
            '/api/v1/add_meetups',
            headers = dict(Authorization = "Bearer " + token),
            json=self.meetups,
            content_type='application/json'
            )
        
        response = self.client.post(
            '/api/v1/1/post_question',
            headers = dict(Authorization = "Bearer " + token),
            json=self.questions, 
            content_type='application/json'
            )

        res = self.client.patch(
            '/api/v1/1/upvote',
            headers = dict(Authorization = "Bearer " + token)
            )
        self.assertEqual(res.status_code, 200)
        self.assertIn(u'1', res.data.decode())

    def test_downvote(self):
        """ test the downvote api """
        self.client.post('/api/v1/user/auth/signup', json=self.users, content_type='application/json')
        results = self.client.post('/api/v1/user/auth/login', json=self.users, content_type='application/json')
        token = json.loads(results.data.decode())['token']
        self.client.post(
            '/api/v1/add_meetups',
            headers = dict(Authorization = "Bearer " + token),
            json=self.meetups,
            content_type='application/json'
            )
        
        response = self.client.post(
            '/api/v1/1/post_question',
            headers = dict(Authorization = "Bearer " + token),
            json=self.questions, 
            content_type='application/json'
            )

        res = self.client.patch(
            '/api/v1/1/downvote',
            headers = dict(Authorization = "Bearer " + token)
            )
        self.assertEqual(res.status_code, 200)
        self.assertIn(u'0', res.data.decode())