from django.urls import path
from .views import TeachersListView, TeachersDetailView

urlpatterns = [

    path('teachers/', TeachersListView.as_view()),

    path('teachers/<int:pk>/', TeachersDetailView.as_view()),

]