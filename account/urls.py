from django.urls import path
from .views import (SendSmsView, ConfirmSmsView, RegistrationView, CountryView, RegionView, AddAddressView,
                    UserView, MedicineView, DoctorView, DeliverAddressView, OfferView)
urlpatterns = [
    path('send/sms/', SendSmsView.as_view()),
    path('send/sms/confirm/', ConfirmSmsView.as_view()),
    path('registration/', RegistrationView.as_view()),
    path('country/', CountryView.as_view()),
    path('region/', RegionView.as_view()),
    path('add/address/', AddAddressView.as_view()),
    path('me/', UserView.as_view()),
    path('favorite/medicines/', MedicineView.as_view()),
    path('favorite/doctors/', DoctorView.as_view()),
    path('deliver/address/', DeliverAddressView.as_view()),
    path('offer/', OfferView.as_view()),

]


