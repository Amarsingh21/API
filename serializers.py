from rest_framework import serializers
# from rest_framework import employees
# from .serializers import employeesSerializer
from . models import employees

class employeesSerializer (serializers.ModelSerializer):
    
    class Meta:
        model = employees
        fields = ('firstname','lastname')
        fields = '__all__'