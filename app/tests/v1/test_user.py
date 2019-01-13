from app.tests.v1.basetest import TestApplication

class TestUser(TestApplication):
    """ Test the user endpoints """
    def test_add_user_successful(self):
        """ Test if user added successfully """
        response = self.client.post('/api/v1/user/auth/signup', json=self.users, content_type='application/json')
        self.assertIn(u'bill', response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_if_no_user_info_provided(self):
        """ Test if user information is previded """
        users={}
        response = self.client.post('/api/v1/user/auth/signup', json=users, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        #Python 3, strings are Unicode, but when transmitting on the network, the data needs to be bytes strings instead
        self.assertIn(u'No data found', response.data.decode())
    
    def test_if_username_is_taken(self):
        """ Test if username s taken """
        self.client.post('/api/v1/user/auth/signup', json=self.users, content_type='application/json')
        response = self.client.post('/api/v1/user/auth/signup', json=self.users_two, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(u'username taken', response.data.decode())

    def test_if_email_is_taken(self):
        """ Test if email is taken """
        self.client.post('/api/v1/user/auth/signup', json=self.users, content_type='application/json')
        response = self.client.post('/api/v1/user/auth/signup', json=self.users_three, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(u'email taken', response.data.decode())

    def test_if_email_is_valid(self):
        """ Test if email is valid """
        response = self.client.post('/api/v1/user/auth/signup', json=self.users_five, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(u'email is not valid', response.data.decode())

    def test_if_password_is_valid(self):
        """ test if password is valid """
        response = self.client.post('/api/v1/user/auth/signup', json=self.users_four, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(u'password is not valid', response.data.decode())