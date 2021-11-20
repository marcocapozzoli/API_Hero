from django.db import models
from employees.models import Base, Employee


class Company(Base):
    company_name = models.CharField(max_length=64)
    trade_name = models.CharField(max_length=64)
    cnpj = models.CharField(max_length=18, unique=True)
    address = models.CharField(max_length=255)
    employees = models.ManyToManyField(Employee)
    
    def __str__(self):
        return self.company_name