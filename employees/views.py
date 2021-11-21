from rest_framework import filters, generics, status
from rest_framework.response import Response

from .models import Employee
from .serializers import CreateEmployeeSerializer, ListEmployeeSerializer


class ListEmployeeAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username']
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ListEmployeeSerializer
        elif self.request.method == 'POST':
            return CreateEmployeeSerializer

class DetailEmployeeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = ListEmployeeSerializer    
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ListEmployeeSerializer(instance)
        return Response(serializer.data)