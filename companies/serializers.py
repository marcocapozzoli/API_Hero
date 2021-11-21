from employees.models import Employee
from rest_framework import serializers
from .validators import validate_cnpj

from .models import Company


class EmployeesCompanySerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    fullname = serializers.CharField(source='get_full_name', read_only=True)    
    class Meta:
        model = Employee
        fields = [
            'id',
            'username',
            'fullname',
            'cpf'
        ]
        
class ListCompanySerializer(serializers.ModelSerializer):
    employees = EmployeesCompanySerializer(
        many=True,
        read_only=True
    )
    class Meta:
        model = Company
        fields = [
            'id',
            'company_name',
            'trade_name',
            'cnpj',
            'address',
            'employees'
        ]