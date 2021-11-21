from rest_framework.test import APITestCase

from ..models import Company
from ..serializers import ListCompanySerializer


class CompanySerializerTestCase(APITestCase):
    
    def setUp(self):
        self.company_attrs = {
            "company_name": "Company Hero",
            "trade_name": "Company Hero S.A",
            "cnpj": "03424020000188",
            "address": "Rua Python, 310"
        }
        self.company = Company.objects.create(**self.company_attrs)
        self.serializer = ListCompanySerializer(instance=self.company)
    
    def test_company_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'company_name', 'trade_name', 'cnpj', 'address', 'employees']))
        
    def test_company_field_contents(self):
        data = self.serializer.data
        self.assertEqual(data['company_name'], self.company.company_name)
        self.assertEqual(data['trade_name'], self.company.trade_name)
        self.assertEqual(data['cnpj'], self.company.cnpj)
        self.assertEqual(data['address'], self.company.address)      
     