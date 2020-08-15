from rest_framework.test import APITestCase
from .models import Manufacturer


class TestManufacturer(APITestCase):
    url = "/vehicle-data/manufacturers"

    def setUp(self):
        Manufacturer.objects.create(name="Toyota", logo="image.png")

    def test_get_manufacturers(self):

        response = self.client.get(self.url)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]["name"], "Toyota")

    def test_post_manufacturers(self):
        # definition
        data = {
            "name": "Honda",
            "logo": "image1.jpg"
        }

        # process
        response = self.client.post(self.url, data=data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["name"], "Honda")

    def test_update_manufacturers(self):
        pk = "1"
        data = {
            "name": "Mercedes Benz"
        }

        response = self.client.patch(self.url + f"/{pk}", data=data)
        result = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(result["name"], "Mercedes Benz")
