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


class LoadsVisitorAvailable(unittest.TestCase):
    '''
    testClass for all page loads for a visitor of the site
    which are available for a visitor
    '''
    # Ensure that the index page loads correctly
    def test_index_loads(self):
        tester = app.test_client()
        response = tester.get(
            '/index',
            content_type='html/text'
        )
        self.assertTrue(b'Welcome to BOS UP' in response.data)

    # Ensure that the vacancies page loads correctly
    def test_vacancies_loads(self):
        tester = app.test_client()
        response = tester.get(
            '/vacancies',
            content_type='html/text'
        )
        self.assertTrue(b'Open Vacancies' in response.data)


class LoadsVisitorUnvailable(unittest.TestCase):
    '''
    testClass for all page loads for a visitor of the site
    which are unavailable for a visitor
    '''
    # Ensure that the error page loads correctly
    def test_addapplicationId_loads(self):
        tester = app.test_client()
        response = tester.get(
            f'/add_application/{VACANCY_ID}',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)

    # Ensure that the error page loads correctly
    def test_addapplication_loads(self):
        tester = app.test_client()
        response = tester.get(
            '/add_application/',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)

    # Ensure that the error page loads correctly
    def test_addapplicationRandomId_loads(self):
        tester = app.test_client()
        response = tester.get(
            '/add_application/abcdefg',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)

    # Ensure that the error page loads correctly
    def test_addapplicationFromApplicationPage(self):
        tester = app.test_client()
        response = tester.get(
            '/add_application/admin',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)

    # Ensure that the error page loads correctly
    def test_adduser(self):
        tester = app.test_client()
        response = tester.get(
            '/add_user',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)

    # Ensure that the error page loads correctly
    def test_addvacancy(self):
        tester = app.test_client()
        response = tester.get(
            '/add_vacancy',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)

    # Ensure that the error page loads correctly
    def test_applications(self):
        tester = app.test_client()
        response = tester.get(
            '/applications',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)

    # Ensure that the error page loads correctly
    def test_changepassword(self):
        tester = app.test_client()
        response = tester.get(
            '/change_password/',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)

    # Ensure that the error page loads correctly
    def test_changepasswordRandomId(self):
        tester = app.test_client()
        response = tester.get(
            '/change_password/abcdefg',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)

    # Ensure that the error page loads correctly
    def test_changepasswordId(self):
        tester = app.test_client()
        response = tester.get(
            f'/change_password/{CANDIDATE_ID_USER}',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)

    # Ensure that the error page loads correctly
    def test_editapplication(self):
        tester = app.test_client()
        response = tester.get(
            '/edit_application',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)

    # Ensure that the error page loads correctly
    def test_editapplicationRandomId(self):
        tester = app.test_client()
        response = tester.get(
            '/edit_application/abcdef',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)

    # Ensure that the error page loads correctly
    def test_editapplicationId(self):
        tester = app.test_client()
        response = tester.get(
            f'/edit_application/{APPLICATION_ID}',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)

    # Ensure that the error page loads correctly
    def test_edituser(self):
        tester = app.test_client()
        response = tester.get(
            '/edit_user',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)

    # Ensure that the error page loads correctly
    def test_edituserRandomId(self):
        tester = app.test_client()
        response = tester.get(
            '/edit_user/abcdef',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)

    # Ensure that the error page loads correctly
    def test_edituserId(self):
        tester = app.test_client()
        response = tester.get(
            f'/edit_user/{CANDIDATE_ID_USER}',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)

    # Ensure that the error page loads correctly
    def test_editvacancy(self):
        tester = app.test_client()
        response = tester.get(
            '/edit_vacancy',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)

    # Ensure that the error page loads correctly
    def test_editvacancyRandomId(self):
        tester = app.test_client()
        response = tester.get(
            '/edit_vacancy/abcdef',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)

    # Ensure that the error page loads correctly
    def test_editvacancyId(self):
        tester = app.test_client()
        response = tester.get(
            f'/edit_vacancy/{VACANCY_ID}',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)

    # Ensure that the error page loads correctly
    def test_profile(self):
        tester = app.test_client()
        response = tester.get(
            '/profile',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)

    # Ensure that the error page loads correctly
    def test_profileRandomdId(self):
        tester = app.test_client()
        response = tester.get(
            '/profile/abcdef',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)

    # Ensure that the error page loads correctly
    def test_profileId(self):
        tester = app.test_client()
        response = tester.get(
            f'/profile/{CANDIDATE_ID_USER}',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)

    # Ensure that the error page loads correctly
    def test_users(self):
        tester = app.test_client()
        response = tester.get(
            '/users',
            content_type='html/text'
        )
        self.assertTrue(b'404 Seems you got lost' in response.data)


# To run the test app
if __name__ == "__main__":
    unittest.main()
