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
        
class DetailCompanyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = ListCompanySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ListCompanySerializer(instance)
        return Response(serializer.data)