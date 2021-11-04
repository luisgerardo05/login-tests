import json
from locust import HttpUser, task, between
from user_data_generator import *


class WebsiteUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def register_route(self):
        name, username, email = create_user()
        with self.client.post(
            url = '/api/users/register',
            data = json.dumps({
                "name": name,
                "email": email,
                "username": username,
                "password": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b",
                "confirm": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b"
            }),
            name='register_route',
            catch_response = True
        ) as response:
            if response.status_code != 200:
                response.failure("Got status code " + str(response.status_code) + " instead of 200")

    @task
    def bad_mail_register_route(self):
        name, username, email = create_user()
        with self.client.post(
            url = '/api/users/register',
            data = json.dumps({
                "name": name,
                "email": username + ".ermiry.com",
                "username": username,
                "password": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b",
                "confirm": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b"
            }),
            name='bad_mail_register_route',
            catch_response = True
        ) as response:
            if response.status_code == 400:
                response.success()
            else:
                response.failure("Got status code " + str(response.status_code) + " instead of 400")

    @task
    def bad_pswd_register_route(self):
        name, username, email = create_user()
        with self.client.post(
            url = '/api/users/register',
            data = json.dumps({
                "name": name,
                "email": email,
                "username": username,
                "password": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b",
                "confirm": username
            }),
            name='bad_pswd_register_route',
            catch_response = True
        ) as response:
            if response.status_code == 400:
                response.success()
            else:
                response.failure("Got status code " + str(response.status_code) + " instead of 400")