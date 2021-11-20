from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Employee(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employees')
    cpf = models.CharField('CPF', max_length=14, unique=True)
   
    def __str__(self):
        return f'{self.user}'