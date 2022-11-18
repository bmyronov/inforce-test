from rest_framework import status
from rest_framework.test import APITestCase


class RegistrationRestaurantTestCase(APITestCase):
    def test_restaurant_registration(self):
        data = {
            "restaurant_name": "some name",
            "email": "test.restaurant@email.com",
            "password": "password",
        }

        response = self.client.post("/api/auth/restaurant/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class EmployeeRestaurantTestCase(APITestCase):
    def test_employee_registration(self):
        data = {
            "email": "test.restaurant@email.com",
            "password": "password",
        }

        response = self.client.post("/api/auth/employee/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
