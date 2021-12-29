from django.contrib.auth.models import User
from rest_framework.test import APITestCase

import base64


class TestApiSetup(APITestCase):
    package_url = 'http://127.0.0.1:8000/package/'

    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="123")
        credentials = base64.b64encode(b'testuser:123').decode("ascii")
        self.client.credentials(HTTP_AUTHORIZATION='Basic ' + credentials)

        return super().setUp()

    def tearDown(self):
        return super().tearDown()