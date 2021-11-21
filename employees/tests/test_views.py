from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class EmployeeAPIViewTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('employees-list')
        self.data = {
            "first_name": "Marco",
            "last_name": "Capozzoli",
            "username": "marcapozzoli",
            "password": "passw0rd3",
            "cpf": "88097396041"
        }
            
    def test_list_employee(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_employee(self):
        response = self.client.post(self.list_url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_employee_with_invalid_cpf(self):
        data = {
            "first_name": "Marco",
            "last_name": "Capozzoli",
            "username": "marcapozzoli",
            "password": "passw0rd3",
            "cpf": "12345678900"
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_employee_with_existing_username(self):
        self.client.post(self.list_url, data=self.data, format='json')
        response = self.client.post(self.list_url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_employee_without_username(self):
        data = {
            "first_name": "Marco",
            "last_name": "Capozzoli",
            "password": "passw0rd3",
            "cpf": "88097396041"
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_employee_without_password(self):
        data = {
            "first_name": "Marco",
            "last_name": "Capozzoli",
            "username": "marcapozzoli",
            "cpf": "88097396041"
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_employee_without_fisrtname(self):
        data = {
            "last_name": "Capozzoli",
            "username": "marcapozzoli",
            "password": "passw0rd3",
            "cpf": "88097396041"
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_employee_without_lastname(self):
        data = {
            "first_name": "Marco",
            "username": "marcapozzoli",
            "password": "passw0rd3",
            "cpf": "88097396041"
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_employee_without_cpf(self):
        data = {
            "first_name": "Marco",
            "last_name": "Capozzoli",
            "username": "marcapozzoli",
            "password": "passw0rd3"
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
