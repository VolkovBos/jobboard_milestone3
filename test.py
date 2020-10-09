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
        response = tester.get('/index', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens vacancies page
    def test_vacancies(self):
        tester = app.test_client(self)
        response = tester.get('/vacancies', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens login page
    def test_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens register page
    def test_register(self):
        tester = app.test_client(self)
        response = tester.get('/register', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that route opens contact page
    def test_contact(self):
        tester = app.test_client(self)
        response = tester.get('/contact', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_addapplication(self):
        tester = app.test_client(self)
        response = tester.get('/addapplication', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_adduser(self):
        tester = app.test_client(self)
        response = tester.get('/adduser', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_addvacancy(self):
        tester = app.test_client(self)
        response = tester.get('/addvacancy', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    # Ensure that a visitor gets the message that this page cannot be found
    def test_applications(self):
        tester = app.test_client(self)
        response = tester.get('/applications', content_type='html/text')
        self.assertEqual(response.status_code, 404)


# To run the test app
if __name__ == "__main__":
    unittest.main()
