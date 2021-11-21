from django.db import models
from employees.models import Base, Employee


class Company(Base):
    company_name = models.CharField(max_length=64, blank=False, unique=True)
    trade_name = models.CharField(max_length=64, blank=False, unique=True)
    cnpj = models.CharField(max_length=18, unique=True)
    address = models.CharField(max_length=255, blank=False)
    employees = models.ManyToManyField(Employee)
    
    def __str__(self):
        return self.company_name