from django.shortcuts import render
# Create your views here.
from .models import Employees
from .serializers import EmployeesSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class EmployeesAPIView(APIView):
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,request):
        employees=Employees.objects.all()
        serializer=EmployeesSerializers(employees,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=EmployeesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
