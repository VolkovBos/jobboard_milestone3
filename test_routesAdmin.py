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


class RoutesAdminAvailable(unittest.TestCase):
    '''
    testClass for all routes for a admin of the site
    which are available for a admin
    '''
    # Ensure that route opens add application page
    def test_addapplicationFromVacancy(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            f'/add_application/{VACANCY_ID}',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens add application page
    def test_addapplicationFromApplicationPage(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            '/add_application/admin',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens add user page
    def test_adduser(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            '/add_user',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens add vacancy page
    def test_addvacancy(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            '/add_vacancy',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens applications page
    def test_applications(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            '/applications',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens change password page
    def test_changepassword(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            f'/change_password/{CANDIDATE_ID_USER}',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens edit application page
    def test_editapplicationId(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            f'/edit_application/{APPLICATION_ID}',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens edit user page
    def test_edituser(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            f'/edit_user/{CANDIDATE_ID_USER}',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens edit vacancy page
    def test_editvacancyId(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            f'/edit_vacancy/{VACANCY_ID}',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens index page
    def test_index(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            '/index',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens my applications page
    def test_myapplications(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            '/myapplications',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens profile page
    def test_profile(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            f'/profile/{CANDIDATE_ID_USER}',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens users page
    def test_users(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            '/users',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens vacancies page
    def test_vacancies(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            '/vacancies',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)


class RoutesAdminUnavailable(unittest.TestCase):
    '''
    testClass for all routes for a admin of the site
    which are unavailable for a admin, mostly due to an incorrect id
    '''
    # Ensure that a admin gets the server error message
    def test_addapplicationFromVacancyFakeId(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            '/add_application/abcdefg',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 500)

    # Ensure that a admin gets the server error message
    def test_changepasswordRandomId(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            '/change_password/abcdef',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 500)

    # Ensure that a admin gets the message that this page cannot be found
    def test_editapplication(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            '/edit_application',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a admin gets the server error message
    def test_editapplicationRandomId(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            '/edit_application/abcdef',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 500)

    # Ensure that a admin gets the server error message
    def test_edituserRandomId(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            '/edit_user/abcdef',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 500)

    # Ensure that a admin gets the message that this page cannot be found
    def test_editvacancy(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            '/edit_vacancy',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a admin gets the server error message
    def test_editvacancyRandomId(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            '/edit_vacancy/abcdef',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 500)

    # Ensure that a admin gets the message that this page cannot be found
    def test_profile(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            '/profile',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a admin gets the server error message
    def test_profileRandomId(self):
        tester = app.test_client()
        tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        response = tester.get(
            '/profile/adbcdef',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 500)


# To run the test app
if __name__ == "__main__":
    unittest.main()
