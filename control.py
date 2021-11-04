import json
from locust import HttpUser, task, between
from user_data_generator import *

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)

    token = ''

    def on_start(self):
        with self.client.post(
            url = '/api/users/login',
            data = json.dumps({
                "email": "erick.salas@verstand.com.mx",
                "password": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b"
            }),
            name = '/api/users/login - on_start',
            catch_response = True
        ) as response:
            self.token = response.json()['token']


    # Admin
    @task
    def top_level_route(self):
        with self.client.get(
            url='/api/users',
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure("Got status code " + str(response.status_code) + " instead of 200")

    @task
    def auth_route(self):
        with self.client.get(
            url='/api/users/auth',
            headers = {'Authorization': self.token},
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure("Got status code " + str(response.status_code) + " instead of 200")

    @task
    def login_route(self):
        with self.client.post(
            url = '/api/users/login',
            data = json.dumps({
                "email": "erick.salas@ermiry.com",
                "password": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b"
            }),
            catch_response = True
        ) as response:
            if response.status_code != 200:
                response.failure("Got status code " + str(response.status_code) + " instead of 200")

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
            catch_response = True
        ) as response:
            if response.status_code != 200:
                response.failure("Got status code " + str(response.status_code) + " instead of 200")

    @task
    def stats_route(self):
        with self.client.get(
            url = '/api/users/cerver/stats',
            headers = {'Authorization': self.token},
            catch_response = True
        ) as response:
            if response.status_code != 200:
                response.failure("Got status code " + str(response.status_code) + " instead of 200")

    @task
    def version_route(self):
        with self.client.get(
            url = '/api/users/version',
            catch_response = True
        ) as response:
            if response.status_code != 200:
                response.failure("Got status code " + str(response.status_code) + " instead of 200")
    