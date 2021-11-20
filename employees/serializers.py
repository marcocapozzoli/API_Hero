from companies.models import Company
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Employee
from .validators import validate_cpf


class CompaniesEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id',
                  'company_name',
                  'trade_name',
                  'cnpj',
                  'address'
        ]

class ListEmployeeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    fullname = serializers.CharField(source='user.get_full_name', read_only=True)
    companies = CompaniesEmployeeSerializer(
        source='company_set',
        many=True,
        read_only=True
    )
    class Meta:
        model = Employee
        fields = [
            'id',
            'username',
            'fullname',
            'cpf',
            'companies'
        ]
