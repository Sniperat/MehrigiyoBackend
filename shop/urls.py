from django.urls import path, include, re_path
from .views import (MedicinesView, TypeMedicineView, GetMedicinesWithType, GetSingleMedicine, CartView,
                    OrderView, AdvertisingView)

urlpatterns = [
    path('types/', TypeMedicineView.as_view()),
    path('types/search/', GetMedicinesWithType.as_view()),
    path('medicines/', MedicinesView.as_view({'list': 'get'})),
    path('advertising/', AdvertisingView.as_view()),
    path('medicines/<int:pk>/', GetSingleMedicine.as_view()),
    path('cart/', CartView.as_view()),
    path('checkout/', OrderView.as_view()),
]
