from django.urls import path
from .views import DoctorsView, TypeDoctorView, GetDoctorsWithType, GetSingleDoctor

urlpatterns = [
    path('types/', TypeDoctorView.as_view()),
    path('types/<int:pk>/', GetDoctorsWithType.as_view()),
    path('doctors/', DoctorsView.as_view()),
    path('doctors/<int:pk>/', GetSingleDoctor.as_view()),
]
