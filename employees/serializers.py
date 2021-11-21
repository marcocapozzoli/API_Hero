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
        
class CreateEmployeeSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    full_name = serializers.CharField(source='user.get_full_name', read_only=True)
    
    class Meta:
        model = Employee
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'password',
            'full_name',
            'cpf'
        ]

    def validate(self, data):
        if not validate_cpf(data.get('cpf', '')):
            raise serializers.ValidationError(
                {'cpf': 'Um cpf válido é obrigatório.'}
            )
        return data
        
    def create(self, validated_data):
        cpf = validated_data.pop('cpf')
        user = User.objects.create(**validated_data)
        instance = Employee.objects.create(user=user, cpf=cpf)
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
    
        instance.user.first_name = validated_data["first_name"]
        instance.user.last_name = validated_data["last_name"]
        instance.user.username = validated_data["username"]
        instance.user.set_password(validated_data["password"])
        instance.user.save()
        instance.cpf = validated_data["cpf"]
        instance.save()
        
        return instance
  
  