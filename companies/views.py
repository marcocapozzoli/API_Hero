from rest_framework import generics, status
from rest_framework.response import Response

from .models import Company
from .serializers import CreateCompanySerializer, ListCompanySerializer


class ListCompanyAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListCompanySerializer
        elif self.request.method == 'POST':
            return CreateCompanySerializer