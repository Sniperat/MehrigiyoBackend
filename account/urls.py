from django.urls import path
from .views import (SendSmsView, ConfirmSmsView, RegistrationView, CountryView, RegionView, AddAddressView,
                    UserView, MedicineView, DoctorView)

urlpatterns = [
    path('send/sms/', SendSmsView.as_view()),
    path('send/sms/confirm/', ConfirmSmsView.as_view()),
    path('registration/', RegistrationView.as_view()),
    path('country/', CountryView.as_view()),
    path('region/', RegionView.as_view()),
    path('add/address/', AddAddressView.as_view()),
    path('me/', UserView.as_view()),
    path('favorite/medicine/<int:pk>/', MedicineView.as_view()),
    path('favorite/doctor/<int:pk>/', DoctorView.as_view()),
]
