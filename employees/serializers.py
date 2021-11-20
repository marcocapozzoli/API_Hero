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
