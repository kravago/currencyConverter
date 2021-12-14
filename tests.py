from app import app
import unittest

class TestCurrencyConverter(unittest.TestCase):

    def test_homepage(self):
        '''Test if the homepage gives a 200 response'''
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

    def test_results(self):
        tester = app.test_client(self)
        response = tester.get('/convert?currency1=USD&currency2=USD&amount=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<p>the result is $1.00</p>', response.data.lower())

    