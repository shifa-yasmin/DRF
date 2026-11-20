from django.urls import path
from .views import EmployeesAPIView

urlpatterns = [
    path('employees/', EmployeesAPIView.as_view()),
]