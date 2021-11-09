import json
from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def login_route(self):
        with self.client.post(
            url = '/api/users/login',
            data = json.dumps({
                "email": "erick.salas@verstand.com.mx",
                "password": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b"
            }),
            name='login_route',
            catch_response = True
        ) as response:
            if response.status_code != 200:
                response.failure("Got status code " + str(response.status_code) + " instead of 200")

    @task
    def bad_email_login_route(self):
        with self.client.post(
            url = '/api/users/login',
            data = json.dumps({
                "email": "erick.salas.verstand.com.mx",
                "password": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b"
            }),
            name='bad_email_login_route',
            catch_response = True
        ) as response:
            if response.status_code == 400:
                response.success()
            else:
                response.failure("Got status code " + str(response.status_code) + " instead of 400")

    @task
    def no_email_login_route(self):
        with self.client.post(
            url = '/api/users/login',
            data = json.dumps({
                "password": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b"
            }),
            name='no_email_login_route',
            catch_response = True
        ) as response:
            if response.status_code == 400:
                response.success()
            else:
                response.failure("Got status code " + str(response.status_code) + " instead of 400")

    @task
    def bad_pswd_login_route(self):
        with self.client.post(
            url = '/api/users/login',
            data = json.dumps({
                "email": "erick.salas@verstand.com.mx",
                "password": "erick.salas@verstand.com.mx"
            }),
            name='bad_pswd_login_route',
            catch_response = True
        ) as response:
            if response.status_code == 400:
                response.success()
            else:
                response.failure("Got status code " + str(response.status_code) + " instead of 400")
    
    @task
    def no_pswd_login_route(self):
        with self.client.post(
            url = '/api/users/login',
            data = json.dumps({
                "email": "erick.salas@verstand.com.mx",
            }),
            name='no_pswd_login_route',
            catch_response = True
        ) as response:
            if response.status_code == 400:
                response.success()
            else:
                response.failure("Got status code " + str(response.status_code) + " instead of 400")

    @task
    def not_registered_login_route(self):
        with self.client.post(
            url = '/api/users/login',
            data = json.dumps({
                "email": "luis.huerta@ermiry.com",
                "password": "049ec1af7c1332193d602986f2fdad5b4d1c2ff90e5cdc65388c794c1f10226b"
            }),
            name='not_registered_login_route',
            catch_response = True
        ) as response:
            if response.status_code == 404:
                response.success()
            else:
                response.failure("Got status code " + str(response.status_code) + " instead of 404")
    