from ..models import Employee
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

class EmployeeModelTesteCase(APITestCase):
    
    def test___str__(self):
        user = User.objects.create_user(
            username="usuario_hero",
            password="password123"
        )
        employee = Employee.objects.create(user=user, cpf='67867987053')
        self.assertEqual(employee.__str__(), employee.user.username)
        self.assertEqual(str(employee), employee.user.username)