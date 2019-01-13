from app.tests.v1.basetest import TestApplication

class TestQuestion(TestApplication):
    """ test the questions endpoints """
    def test_add_question_successful(self):
        """ test if question is successfuly added """
        response = self.client.post('/api/v1/1/post_question', json=self.questions, content_type='application/json')
        self.assertIn(u'ill@wek', response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_add_question_failure(self):
        """ test if question fails validation """
        questions = {}
        response = self.client.post('/api/v1/1/post_question', json=questions, content_type='application/json')
        self.assertIn(u'No data found', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_if_question_data_available(self):
        """ test if specific question id is existent """
        response = self.client.post('/api/v1/add_meetups', json=self.question_one, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(u'tags is missing', response.data.decode())

    def test_upvote(self):
        """ test the upvote api """
        response = self.client.post('/api/v1/1/upvote', json=self.upvote, content_type='application/json')
        self.assertEqual(response.status_code, 405)
        self.assertIn(u'1', response.data.decode())

    def test_downvote(self):
        """ test the downvote api """
        response = self.client.post('/api/v1/1/downvote', json=self.upvote, content_type='application/json')
        self.assertEqual(response.status_code, 405)
        self.assertIn(u'0', response.data.decode())