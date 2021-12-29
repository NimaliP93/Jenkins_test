from rest_framework import status

from test.test_setup import TestApiSetup


class TestPackageViewSet(TestApiSetup):
    def test_get_package_authenticated(self):
        response = self.client.get(self.package_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_package_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.package_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_package_authenticated(self):
        data = {
            'pkg_name': "name with test",
            'pkg_code': 'test code',
            'display_name': 'test display name',
            'status': True,
            'global_enable': True
        }

        response = self.client.post(self.package_url, data, format("json"))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['pkg_name'], 'name with test')

