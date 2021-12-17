from app import app
import unittest

class TestCurrencyConverter(unittest.TestCase):

    def test_homepage(self):
        '''Test if the homepage gives a 200 response'''
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)


    def test_with_valid_data(self):
        tester = app.test_client(self)
        response = tester.get('/convert', query_string=dict(currency1='USD', currency2='USD', amount=1))

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<p>the result is $1.00</p>', response.data.lower())


    def test_with_invalid_currency1(self):
        tester = app.test_client(self)
        response = tester.get('/convert',
                                query_string=dict(currency1='wha', currency2='USD', amount=1),
                                follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<p class="alert">wha is not a valid currency code</p>', response.data.lower())


    def test_with_invalid_data(self):
        tester = app.test_client(self)
        response = tester.get('/convert',
                                query_string=dict(currency1='123', currency2='456', amount='$'),
                                follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<p class="alert">123 is not a valid currency code</p>', response.data.lower())
        self.assertIn(b'<p class="alert">456 is not a valid currency code</p>', response.data.lower())
        self.assertIn(b'<p class="alert">$ is an invalid amount</p>', response.data.lower())
