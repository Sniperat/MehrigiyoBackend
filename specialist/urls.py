from django.urls import path
from .views import (DoctorsView, TypeDoctorView, GetDoctorsWithType, GetSingleDoctor, AdviceView, AdvertisingView,
                    DoctorFilterView)

urlpatterns = [
    path('types/', TypeDoctorView.as_view()),
    path('types/<int:pk>/', GetDoctorsWithType.as_view()),
    path('doctors/', DoctorsView.as_view()),
    path('doctors/filter/', DoctorFilterView.as_view()),
    path('advertising/', AdvertisingView.as_view()),
    path('doctors/<int:pk>/', GetSingleDoctor.as_view()),
    path('advice/<int:pk>/', AdviceView.as_view()),
]
