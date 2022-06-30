from django.urls import path
from .views import (DoctorsView, TypeDoctorView, GetDoctorsWithType, GetSingleDoctor, AdviceView, AdvertisingView)

urlpatterns = [
    path('types/', TypeDoctorView.as_view()),
    path('types/<int:pk>/', GetDoctorsWithType.as_view()),
    path('doctors/', DoctorsView.as_view({'list': 'get'})),
    path('advertising/', AdvertisingView.as_view()),
    path('doctors/<int:pk>/', GetSingleDoctor.as_view()),
    path('advice/<int:pk>/', AdviceView.as_view()),
]
