from app.tests.v1.basetest import TestApplication

class TestMeetup(TestApplication):
    """ test the meetup endpoints"""
    def test_add_meetup_successful(self):
        """ test if meetups are added successfuly """
        response = self.client.post('/api/v1/add_meetups', json=self.meetups, content_type='application/json')
        self.assertIn(u'online', response.data.decode())
        self.assertEqual(response.status_code, 201)

    def test_add_meetup_failure(self):
        """ test if meetups addition fail """
        meetups = {}
        response = self.client.post('/api/v1/add_meetups', json=meetups, content_type='application/json')
        self.assertIn(u'No data found', response.data.decode())
        self.assertEqual(response.status_code, 400)

    def test_get_meetups_sucessful(self):     
        """ test if meetups are returned on call """   
        response = self.client.get('/api/v1/get_meetups')
        self.assertIn(u'online', response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_get_meetup_failure(self):
        """ confirms the status response on failure """
        meetups = {}
        response = self.client.get('/api/v1/get_meetups', json=meetups, content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_get_specific_meetup_sucessful(self):
        """ test if specific meetup can be obtained """
        response = self.client.get('/api/v1/meetups/1')
        self.assertIn(u'online', response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_create_reservation(self):
        """ test if reservatios are created """
        response = self.client.post('/api/v1/1/attend', json=self.reservation, content_type='application/json')
        self.assertIn(u'YES', response.data.decode())
        self.assertEqual(response.status_code, 200)

    def test_if_meetup_data_available(self):
        """ test if meetup fields are available """
        response = self.client.post('/api/v1/add_meetups', json=self.meetups_one, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(u'location is missing', response.data.decode())

    def test_if_meetup_field_available(self):
        """ test if meetup data is available """
        response = self.client.post('/api/v1/add_meetups', json=self.meetups_two, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(u'location is missing', response.data.decode())