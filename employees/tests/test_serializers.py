from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from ..models import Employee
from ..serializers import ListEmployeeSerializer


class EmployeeSerializerTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username="usuario_hero",
            password="password123"
        )
        self.employee_attrs = {
            "user": self.user,
            "cpf": "67867987053"
        }
        self.employee = Employee.objects.create(**self.employee_attrs)
        self.serializer = ListEmployeeSerializer(instance=self.employee)
    
    def test_employee_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'username', 'fullname', 'cpf', 'companies']))
        
    def test_employee_field_contents(self):
        data = self.serializer.data
        self.assertEqual(data['username'], self.employee.user.username)
        self.assertEqual(data['cpf'], self.employee.cpf)
        self.assertEqual(data['fullname'], self.employee.user.get_full_name())      