from django.contrib import admin
from django.urls import path
from employees.views import ListEmployeeAPIView, DetailEmployeeAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'employees': reverse('employees-list', request=request, format=format),
    })
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', api_root),
    path('v1/employees/', ListEmployeeAPIView.as_view(), name='employees-list'),
    path('v1/employee/<int:pk>/', DetailEmployeeAPIView.as_view(), name='employees-detail'),
]

