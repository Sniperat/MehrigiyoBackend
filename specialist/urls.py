from django.urls import path
from .views import (DoctorsView, TypeDoctorView, GetDoctorsWithType, GetSingleDoctor, AdviceView, AdvertisingView)

urlpatterns = [
    path('types/', TypeDoctorView.as_view({'list': 'get'})),
    path('types/one/', GetDoctorsWithType.as_view({'list': 'get'})),
    path('doctors/', DoctorsView.as_view({'list': 'get'})),
    path('advertising/', AdvertisingView.as_view()),
    path('doctors/one/', GetSingleDoctor.as_view({'list': 'get'})),
    path('advice/<int:pk>/', AdviceView.as_view()),
]
