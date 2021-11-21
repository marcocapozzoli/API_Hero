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

class CreateCompanySerializer(serializers.ModelSerializer):   
    
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
        extra_kwargs = {
            "employees": {
                "required": False,
                "allow_null": True
            }
        }
    
       
    def validate(self, data):
        
        if Company.objects.filter(company_name=data['company_name']):
            raise serializers.ValidationError({
                "company_name": f"Uma empresa com razão social `{data['company_name']}` " + "já encontra-se cadastrada no banco de dados."
            })
        if Company.objects.filter(trade_name=data['trade_name']):
            raise serializers.ValidationError({
                "trade_name": f"Uma empresa com nome fantasia `{data['trade_name']}` " + "já encontra-se cadastrada no banco de dados."
            })
        if not validate_cnpj(data.get('cnpj', '')):
            raise serializers.ValidationError(
                {'cnpj': 'Um cnpj válido é obrigatório.'}
            )
        if Company.objects.filter(cnpj=data['cnpj']):
            raise serializers.ValidationError({
                "cnpj": f"Uma empresa com cnpj `{data['cnpj']}` " + "já encontra-se cadastrada no banco de dados."
            })
        return data
    
    def create(self, validated_data):
         
        if validated_data.get('employees'):
            employees = validated_data.pop('employees')   
            instance = Company.objects.create(**validated_data)
            for employee in employees:
                instance.employees.add(employee)
        else: 
            instance = Company.objects.create(**validated_data)
            instance.employees.set = []

        return instance
    
    def update(self, instance, validated_data):

        if validated_data.get('employees'):
            employees = validated_data.pop('employees')
            for employee in employees:
                instance.employees.add(employee)
                
        instance.company_name = validated_data["company_name"]
        instance.trade_name = validated_data["trade_name"]
        instance.cnpj = validated_data["cnpj"]
        instance.address = validated_data["address"]
        instance.save()
        
        return instance
  
  
        