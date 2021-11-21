from ..models import Company
from rest_framework.test import APITestCase

class CompanyModelTesteCase(APITestCase):
    
    def test___str__(self):
        company = Company.objects.create(
            company_name="Company Hero",
            trade_name="Company Hero S.A",
            cnpj="42340981000166",
            address="Rua python, 310",
        )
        self.assertEqual(company.__str__(), company.company_name)
        self.assertEqual(str(company), company.company_name)