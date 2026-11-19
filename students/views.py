from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from students.models import Student
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializers

class StudentAPIView(APIView):
    def get(self,request):
        students=Student.objects.all()
        serializer=StudentSerializers(students,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)