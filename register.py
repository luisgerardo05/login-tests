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
    def no_name_register_route(self):
        name, username, email = create_user()
        with self.client.post(
            url = '/api/users/register',
            data = json.dumps({
                "email": email,
                "username": username,
                "password": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b",
                "confirm": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b"
            }),
            name='no_name_register_route',
            catch_response = True
        ) as response:
            if response.status_code == 400:
                response.success()
            else:
                response.failure("Got status code " + str(response.status_code) + " instead of 400")
    
    @task
    def no_email_register_route(self):
        name, username, email = create_user()
        with self.client.post(
            url = '/api/users/register',
            data = json.dumps({
                "name": name,
                "username": username,
                "password": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b",
                "confirm": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b"
            }),
            name='no_email_register_route',
            catch_response = True
        ) as response:
            if response.status_code == 400:
                response.success()
            else:
                response.failure("Got status code " + str(response.status_code) + " instead of 400")
    
    @task
    def no_username_register_route(self):
        name, username, email = create_user()
        with self.client.post(
            url = '/api/users/register',
            data = json.dumps({
                "name": name,
                "email": email,
                "password": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b",
                "confirm": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b"
            }),
            name='no_username_register_route',
            catch_response = True
        ) as response:
            if response.status_code == 400:
                response.success()
            else:
                response.failure("Got status code " + str(response.status_code) + " instead of 400")

    @task
    def no_password_register_route(self):
        name, username, email = create_user()
        with self.client.post(
            url = '/api/users/register',
            data = json.dumps({
                "name": name,
                "email": email,
                "username": username,
                "confirm": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b"
            }),
            name='no_password_register_route',
            catch_response = True
        ) as response:
            if response.status_code == 400:
                response.success()
            else:
                response.failure("Got status code " + str(response.status_code) + " instead of 400")
    
    @task
    def no_confirm_register_route(self):
        name, username, email = create_user()
        with self.client.post(
            url = '/api/users/register',
            data = json.dumps({
                "name": name,
                "email": email,
                "username": username,
                "password": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b",
            }),
            name='no_confirm_register_route',
            catch_response = True
        ) as response:
            if response.status_code == 400:
                response.success()
            else:
                response.failure("Got status code " + str(response.status_code) + " instead of 400")

    @task
    def invalid_email_text_register_route(self):
        name, username, email = create_user()
        with self.client.post(
            url = '/api/users/register',
            data = json.dumps({
                "name": name,
                "email": name,
                "username": username,
                "password": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b",
                "confirm": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b"
            }),
            name='invalid_email_text_register_route',
            catch_response = True
        ) as response:
            if response.status_code == 400:
                response.success()
            else:
                response.failure("Got status code " + str(response.status_code) + " instead of 400")

    @task
    def invalid_email_register_route(self):
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
            name='invalid_email_register_route',
            catch_response = True
        ) as response:
            if response.status_code == 400:
                response.success()
            else:
                response.failure("Got status code " + str(response.status_code) + " instead of 400")

    @task
    def bad_domain_register_route(self):
        name, username, email = create_user()
        with self.client.post(
            url = '/api/users/register',
            data = json.dumps({
                "name": name,
                "email": username + "@example",
                "username": username,
                "password": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b",
                "confirm": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b"
            }),
            name='bad_domain_register_route',
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