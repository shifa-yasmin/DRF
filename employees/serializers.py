from rest_framework import serializers
from .models import Employees

class EmployeesSerializers(serializers.ModelSerializer):
    class Meta:
        models=Employees
        fields="__all__"