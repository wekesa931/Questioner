from app.tests.v2.basetest import TestApplication
import json

class TestQuestion(TestApplication):
    """ test the questions endpoints """
    
    def test_add_question_successful(self):
        """ test if question is successfuly added """
        results = self.client.post('/api/v2/user/auth/login', json=self.super_user, content_type='application/json')
        token = json.loads(results.data.decode())['data'][0]['token']
        self.client.post(
            '/api/v2/meetups',
            headers = dict(Authorization = "Bearer " + token),
            json=self.meetups,
            content_type='application/json'
            )
        response = self.client.post(
            '/api/v2/1/question',
            headers = dict(Authorization = "Bearer " + token),
            json=self.questions, 
            content_type='application/json'
            )
        self.assertIn(u'ill@wek', response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_add_question_failure(self):
        """ test if question fails validation """
        questions = {}
        results = self.client.post('/api/v2/user/auth/login', json=self.super_user, content_type='application/json')
        token = json.loads(results.data.decode())['data'][0]['token']
        self.client.post(
            '/api/v2/meetups',
            headers = dict(Authorization = "Bearer " + token),
            json=self.meetups,
            content_type='application/json'
            )

        response = self.client.post(
            '/api/v2/1/question',
            headers = dict(Authorization="Bearer " + token),
            json=questions,
            content_type='application/json'
            )
        self.assertIn(u'No data found', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_if_question_data_available(self):
        """ test if specific question id is existent """
        results = self.client.post('/api/v2/user/auth/login', json=self.super_user, content_type='application/json')
        token = json.loads(results.data.decode())['data'][0]['token']
        self.client.post(
            '/api/v2/meetups',
            headers = dict(Authorization = "Bearer " + token),
            json=self.meetups,
            content_type='application/json'
            )
        response = self.client.post(
            '/api/v2/1/question',
            headers = dict(Authorization="Bearer " + token),
            json=self.question_one, 
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 400)
        self.assertIn(u'title is missing a value', response.data.decode())

    def test_if_question_field_available(self):
        """ test if specific question id is existent """
        results = self.client.post('/api/v2/user/auth/login', json=self.super_user, content_type='application/json')
        token = json.loads(results.data.decode())['data'][0]['token']
        self.client.post(
            '/api/v2/meetups',
            headers = dict(Authorization = "Bearer " + token),
            json=self.meetups,
            content_type='application/json'
            )
        response = self.client.post(
            '/api/v2/1/question',
            headers = dict(Authorization="Bearer " + token),
            json=self.question_two, 
            content_type='application/json'
            )
        self.assertEqual(response.status_code, 400)
        self.assertIn(u'title is missing', response.data.decode())

    def test_upvote(self):
        """ test the upvote api """
        results = self.client.post('/api/v2/user/auth/login', json=self.super_user, content_type='application/json')
        token = json.loads(results.data.decode())['data'][0]['token']
        self.client.post(
            '/api/v2/meetups',
            headers = dict(Authorization = "Bearer " + token),
            json=self.meetups,
            content_type='application/json'
            )
        
        response = self.client.post(
            '/api/v2/1/question',
            headers = dict(Authorization = "Bearer " + token),
            json=self.questions, 
            content_type='application/json'
            )

        res = self.client.patch(
            '/api/v2/1/upvote',
            headers = dict(Authorization = "Bearer " + token),
            json=self.vote, 
            content_type='application/json'
            )
        self.assertIn(u'1', res.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_downvote(self):
        """ test the downvote api """
        results = self.client.post('/api/v2/user/auth/login', json=self.super_user, content_type='application/json')
        token = json.loads(results.data.decode())['data'][0]['token']
        self.client.post(
            '/api/v2/meetups',
            headers = dict(Authorization = "Bearer " + token),
            json=self.meetups,
            content_type='application/json'
            )
        
        response = self.client.post(
            '/api/v2/1/question',
            headers = dict(Authorization = "Bearer " + token),
            json=self.questions, 
            content_type='application/json'
            )

        res = self.client.patch(
            '/api/v2/1/downvote',
            headers = dict(Authorization = "Bearer " + token)
            )
        self.assertIn(u'0', res.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_add_comment(self):
        """ test the downvote api """
        results = self.client.post('/api/v2/user/auth/login', json=self.super_user, content_type='application/json')
        token = json.loads(results.data.decode())['data'][0]['token']
        self.client.post(
            '/api/v2/meetups',
            headers = dict(Authorization = "Bearer " + token),
            json=self.meetups,
            content_type='application/json'
            )
        
        response = self.client.post(
            '/api/v2/1/question',
            headers = dict(Authorization = "Bearer " + token),
            json=self.questions, 
            content_type='application/json'
            )

        res = self.client.post(
            '/api/v2/1/comment',
            headers = dict(Authorization = "Bearer " + token),
            json=self.comment, 
            content_type='application/json'
            )
        self.assertIn(u'welcome', res.data.decode())
        self.assertEqual(response.status_code, 201)