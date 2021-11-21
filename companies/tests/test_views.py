from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CompanyViewTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('companies-list')
        self.data = {
            "company_name": "Company Hero",
            "trade_name": "Company Hero S.A",
            "cnpj": "02711608000150",
            "address": "Rua Python, 310",
        }
            
    def test_list_company(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_company(self):
        response = self.client.post(self.list_url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_company_with_invalid_cnpj(self):
        data = {
            "company_name": "Company Hero",
            "trade_name": "Company Hero S.A",
            "cnpj": "12345678901234",
            "address": "Rua Python, 310"
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_company_with_existing_cnpj(self):
        self.client.post(self.list_url, data=self.data, format='json')
        response = self.client.post(self.list_url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_company_without_company_name(self):
        data = {
            "trade_name": "Company Hero S.A",
            "cnpj": "03424020000188",
            "address": "Rua Python, 310"
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_company_without_trade_name(self):
        data = {
            "company_name": "Company Hero",
            "cnpj": "03424020000188",
            "address": "Rua Python, 310"
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_company_without_cnpj(self):
        data = {
            "company_name": "Company Hero",
            "trade_name": "Company Hero S.A",
            "address": "Rua Python, 310"
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_company_without_address(self):
        data = {
            "company_name": "Company Hero",
            "trade_name": "Company Hero S.A",
            "cnpj": "03424020000188"
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_create_company_without_employees(self):
        data = {
            "company_name": "Company Hero",
            "trade_name": "Company Hero S.A",
            "cnpj": "03424020000188",
            "address": "Rua Python, 310"
        }
        response = self.client.post(self.list_url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
           