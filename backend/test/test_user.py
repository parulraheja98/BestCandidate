import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 


from app import app
import unittest
import json
import time
import uuid
import pytest


class TestUserRegister(unittest.TestCase):

    def test_register(self):
        tester = app.test_client(self)
        response = tester.post('/register', data=dict(username='testcheck15',password='gomez',role='user',firstname='selena',lastname='gomez'))
        resp = response.get_json()
        assert len(resp['message']) > 0


class TestUserLogin(unittest.TestCase):

    def test_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username='testcheck15',password='gomez'))
        resp = response.get_json()
        assert len(resp['access_token']) > 0 and len(resp['refresh_token']) > 0 and resp['id'] > 0

class TestCreateApplication(unittest.TestCase):

    def test_create_application(self):
        tester = app.test_client(self)
        response = tester.post('/applications', data=dict(user=3,job=1))
        resp = response.get_json()
        self.assertIn('Application Created Successfully', resp['message']) 

class TestCreateJob(unittest.TestCase):

    def test_create_job(self):
        tester = app.test_client(self)
        response = tester.post('/jobs', data=dict(
        title='Software Designer',
        description='Design the overall architecture',
        posted_by=1,
        status='ongoing',
        date_posted='2019-07-21T23:13:3',
        deadline='2019-07-23T23:13:3'
        ))
        resp = response.get_json()
        self.assertIn('Job successfully created', resp['message']) 
    




    


if __name__ == '__main__':
    unittest.main()