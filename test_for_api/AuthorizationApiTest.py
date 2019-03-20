import time
import unittest
import requests


class AuthorizationApiTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_email = 'autotest' + str(time.time()) + '@test.com'
        cls.test_phone_number = '06' + str(time.time()).replace('.', '')[2:10]
        cls.test_password = 'Qwe123456'
        cls.headers = {
            'content-type': 'application/json',
            'app_platform': 'Web',
            'accept-language': 'uk-UA,uk;q=0.9,ru;q=0.8,en-US;q=0.7,en;q=0.6',
            'app_version': '0.1.0',
            'x-device-identifier': '8d81a06b80d4efce32e9314561a2e85e'
        }
        cls.signin_url = 'https://welcome.kapten.com/api/riders/login'
        cls.signup_url = 'https://welcome.kapten.com/api/riders/signup'

    def test_successful_signup_and_signin(self):
        signup_body = {
            "email": self.test_email,
            "password": self.test_password,
            "first_name":"test",
            "last_name":"test",
            "phone_data":{
                "iso_code":"FR",
                "country_code":"33",
                "number":self.test_phone_number},
            "tracking":{}}

        response = requests.post(self.signup_url, json=signup_body, headers=self.headers)

        assert response.status_code==200
        assert 'token' in response.json()
        assert 'id' in response.json()

        #check that user can signin now

        signin_body = {
            "email":self.test_email,
            "password":self.test_password,
            "tracking":{}}

        response = requests.post(self.signin_url, json=signin_body, headers=self.headers)

        assert response.status_code == 200, response.json()

    def test_signin_with_invalid_credentials(self):
        signin_body = {
            "email": self.test_email,
            "password": '111111Qwe',
            "tracking": {}}

        response = requests.post(self.signin_url, json=signin_body, headers=self.headers)

        assert response.status_code == 401, response.json()
        assert 'login has failed' in response.json()['message']
        assert 'FAILED_LOGIN' in response.json()['code']

