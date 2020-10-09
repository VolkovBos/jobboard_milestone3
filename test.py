# Imports needed
import os
from app import app
import unittest


# Import my env.py that's ignored by git
if os.path.exists("env.py"):
    import env


class RoutesVisitor(unittest.TestCase):
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


class FlaskTestCasesLoadsVisitor(unittest.TestCase):
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


# To run the test app
if __name__ == "__main__":
    unittest.main()
