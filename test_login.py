# Imports needed
import os
from flask_pymongo import PyMongo
from app import app
import unittest


# Import my env.py that's ignored by git
if os.path.exists("env.py"):
    import env


# Set usernames and passwords for login tests
USERNAME_ADMIN = os.environ.get('USERNAME_ADMIN')
USERNAME_USER = os.environ.get('USERNAME_USER')
SPW_ONE = os.environ.get('SPW_ONE')
SPW_TWO = os.environ.get('SPW_TWO')


# MongoDB configuration
mongo = PyMongo(app)
vacancy = mongo.db.vacancies.find_one()
candidate_user = mongo.db.candidates.find_one({'user_name': USERNAME_USER})
candidate_admin = mongo.db.candidates.find_one({'user_name': USERNAME_ADMIN})
application = mongo.db.applications.find_one()


VACANCY_ID = vacancy['_id']
CANDIDATE_ID_USER = candidate_user['_id']
CANDIDATE_NAME_USER = candidate_user['first_name'] \
    + candidate_user['last_name']
CANDIDATE_ID_ADMIN = candidate_admin['_id']
APPLICATION_ID = application['_id']


class LoginUserTests(unittest.TestCase):
    '''
    testClass for user login functionality
    '''
    # Test for login by user with correct credentials
    def test_correct_credentials_user(self):
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username=USERNAME_USER, password=SPW_TWO),
            follow_redirects=True
        )
        self.assertIn(b'Welcome to BOS UP', response.data)

    # Test for login by user with incorrect username
    def test_incorrect_username_user(self):
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username='randomusername', password=SPW_TWO),
            follow_redirects=True
        )
        self.assertIn(b'The username provided is not known', response.data)

    # Test for login by user with incorrect password
    def test_incorrect_password_user(self):
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username=USERNAME_USER, password='randompassword'),
            follow_redirects=True
        )
        self.assertIn(b'Your password is incorrect', response.data)
    ''' Not wokring yet
    # Test for login by user with unapproved status
    def test_upprovedUser(self):
        tester = app.test_client()
        # candidate_user['approved'] = False
        response = tester.post(
            '/login',
            data=dict(username=USERNAME_USER, password=SPW_TWO),
            follow_redirects=True
        )
        self.assertIn(b'Your registration is not processed yet.', response.data)
    '''
    # Test for logout by user
    def test_correct_logout(self):
        tester = app.test_client(self)
        tester.post(
            '/login',
            data=dict(username=USERNAME_USER, password=SPW_TWO),
            follow_redirects=True
        )
        response = tester.get('/logout', follow_redirects=True)
        self.assertTrue(b'Welcome to BOS UP' in response.data)


class LoginAdminTests(unittest.TestCase):
    '''
    testClass for admin login functionality
    '''
    # Test for login by admin with correct credentials
    def test_correct_credentials_admin(self):
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        self.assertIn(b'Welcome to BOS UP', response.data)

    # Test for login by admin with incorrect username
    def test_incorrect_username_admin(self):
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username='randomusername', password=SPW_ONE),
            follow_redirects=True
        )
        self.assertIn(b'The username provided is not known', response.data)

    # Test for login by admin with incorrect password
    def test_incorrect_password_admin(self):
        tester = app.test_client()
        response = tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password='randompassword'),
            follow_redirects=True
        )
        self.assertIn(b'Your password is incorrect', response.data)

    # Test for logout by admin
    def test_correct_logout(self):
        tester = app.test_client(self)
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get('/logout', follow_redirects=True)
        self.assertTrue(b'Welcome to BOS UP' in response.data)


# To run the test app
if __name__ == "__main__":
    unittest.main()
