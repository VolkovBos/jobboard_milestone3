# Imports needed
import os
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


'''
testClass for all routes for a visitor of the site
which are available for a visitor
'''
class RoutesVisitorAvailable(unittest.TestCase):
    # Ensure that route opens index page
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get(
            '/index',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens vacancies page
    def test_vacancies(self):
        tester = app.test_client(self)
        response = tester.get(
            '/vacancies',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens login page
    def test_login(self):
        tester = app.test_client(self)
        response = tester.get(
            '/login',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens register page
    def test_register(self):
        tester = app.test_client(self)
        response = tester.get(
            '/register',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens contact page
    def test_contact(self):
        tester = app.test_client(self)
        response = tester.get(
            '/contact',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 200)


'''
testClass for all routes for a visitor of the site
which are unavailable for a visitor
'''
'''
class RoutesVisitorUnavailable(unittest.TestCase):
    # Ensure that a visitor gets the message that this page cannot be found
    def test_addapplicationFromVacancie(self):
        tester = app.test_client(self)
        response = tester.get(
            '/add_application/abcdefg',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_addapplicationFromApplicationPage(self):
        tester = app.test_client(self)
        response = tester.get(
            '/add_application/admin',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_adduser(self):
        tester = app.test_client(self)
        response = tester.get(
            '/add_user',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_addvacancy(self):
        tester = app.test_client(self)
        response = tester.get(
            '/add_vacancy',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_applications(self):
        tester = app.test_client(self)
        response = tester.get(
            '/applications',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_changepassword(self):
        tester = app.test_client(self)
        response = tester.get(
            '/change_password/abcdefg',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_editapplications(self):
        tester = app.test_client(self)
        response = tester.get(
            '/edit_application',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_editusers(self):
        tester = app.test_client(self)
        response = tester.get(
            '/edit_user',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_editvacancy(self):
        tester = app.test_client(self)
        response = tester.get(
            '/edit_vacancy',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_profile(self):
        tester = app.test_client(self)
        response = tester.get(
            '/profile',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_users(self):
        tester = app.test_client(self)
        response = tester.get(
            '/users',
            content_type='html/text'
        )
        self.assertEqual(response.status_code, 404)
'''


# testClass for all page loads for a visitor of the site
class loadsVisitor(unittest.TestCase):
    # Ensure that the index page loads correctly
    def test_index_loads(self):
        tester = app.test_client(self)
        response = tester.get(
            '/index',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>Welcome to BOS UP</h1>' in response.data)

    # Ensure that the vacancies page loads correctly
    def test_vacancies_loads(self):
        tester = app.test_client(self)
        response = tester.get(
            '/vacancies',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>Open Vacancies</h1>' in response.data)

    # Ensure that the login page loads correctly
    def test_login_loads(self):
        tester = app.test_client(self)
        response = tester.get(
            '/login',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>Login Page</h1>' in response.data)

    # Ensure that the register page loads correctly
    def test_register_loads(self):
        tester = app.test_client(self)
        response = tester.get(
            '/register',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>Registration</h1>' in response.data)

    # Ensure that the contact page loads correctly
    def test_contact_loads(self):
        tester = app.test_client(self)
        response = tester.get(
            '/contact',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>Contact Us</h1>' in response.data)
'''
    # Ensure that the error page loads correctly
    def test_addapplication_loads(self):
        tester = app.test_client(self)
        response = tester.get(
            '/add_application/abcdefg',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_addapplicationFromApplicationPage(self):
        tester = app.test_client(self)
        response = tester.get(
            '/add_application/admin',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_adduser(self):
        tester = app.test_client(self)
        response = tester.get(
            '/add_user',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_addvacancy(self):
        tester = app.test_client(self)
        response = tester.get(
            '/add_vacancy',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_applications(self):
        tester = app.test_client(self)
        response = tester.get(
            '/applications',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_changepassword(self):
        tester = app.test_client(self)
        response = tester.get(
            '/change_password/abcdefg',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_editapplications(self):
        tester = app.test_client(self)
        response = tester.get(
            '/edit_application',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_editusers(self):
        tester = app.test_client(self)
        response = tester.get(
            '/edit_user',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_editvacancy(self):
        tester = app.test_client(self)
        response = tester.get(
            '/edit_vacancy',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_profile(self):
        tester = app.test_client(self)
        response = tester.get(
            '/profile',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)

    # Ensure that the error page loads correctly
    def test_users(self):
        tester = app.test_client(self)
        response = tester.get(
            '/users',
            content_type='html/text'
        )
        self.assertTrue(b'<h1>404 Seems you got lost</h1>' in response.data)
'''


# testClass for all login functionality
class loginTests(unittest.TestCase):
    # Test for login by user with correct credentials
    def test_correct_credentials_user(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username=USERNAME_USER, password=SPW_TWO),
            follow_redirects=True
        )
        self.assertIn(b'<h1>Welcome to BOS UP</h1>', response.data)

    # Test for login by user with incorrect username
    def test_incorrect_username_user(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username='randomusername', password=SPW_TWO),
            follow_redirects=True
        )
        self.assertIn(b'The username provided is not known', response.data)

    # Test for login by user with incorrect password
    def test_incorrect_password_user(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username=USERNAME_USER, password='randompassword'),
            follow_redirects=True
        )
        self.assertIn(b'Your password is incorrect', response.data)

    # Test for login by admin with correct credentials
    def test_correct_credentials_admin(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password=SPW_ONE),
            follow_redirects=True
        )
        self.assertIn(b'<h1>Welcome to BOS UP</h1>', response.data)

    # Test for login by admin with incorrect username
    def test_incorrect_username_admin(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username='randomusername', password=SPW_ONE),
            follow_redirects=True
        )
        self.assertIn(b'The username provided is not known', response.data)

    # Test for login by admin with incorrect password
    def test_incorrect_password_admin(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username=USERNAME_ADMIN, password='randompassword'),
            follow_redirects=True
        )
        self.assertIn(b'Your password is incorrect', response.data)


# To run the test app
if __name__ == "__main__":
    unittest.main()
