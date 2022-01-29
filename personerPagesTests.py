import unittest
from flask import Flask, render_template, request, url_for, redirect
from app import app
from models import db, Person


class PersonerTestCases(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        #self.client = app.test_client()
        app.config["SERVER_NAME"] = "stefan.se"
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['WTF_CSRF_METHODS'] = []  # This is the magic
        app.config['TESTING'] = True

    def tearDown(self):
        #self.ctx.pop()
        pass

    def test_when_creating_new_should_validate_name_is_longer_than_three(self):
        test_client = app.test_client()
        with test_client:
            url = 'personer/new'
            response = test_client.post(url, data={ "name":"12", "city":"Testar", "postalcode":"11122", "position":"g" })
            assert url.endswith(request.path)

    def test_when_creating_new_should_be_ok_when_name_is_longer_than_three(self):
        test_client = app.test_client()
        with test_client:
            url = 'personer/new'
            response = test_client.post(url, data={ "name":"Stefan", "city":"Testar", "postalcode":"11122", "position":"g" })
            assert response.status == 302




if __name__ == "__main__":
    unittest.main()