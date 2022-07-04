from django.urls import path, include, re_path
from rest_framework import routers

from .views import (MedicinesView, TypeMedicineView, GetMedicinesWithType, GetSingleMedicine, CartView,
                    OrderView, AdvertisingView)
# router = routers.DefaultRouter()
# router.register(r'medicines', MedicinesView)

urlpatterns = [
    # path('', include(router.urls)),
    path('types/', TypeMedicineView.as_view({'list': 'get'})),
    path('types/search/', GetMedicinesWithType.as_view({"post": "get_with_types"})),
    path('medicines/', MedicinesView.as_view({'list': 'get'})),
    path('advertising/', AdvertisingView.as_view()),
    # path('medicines/<int:pk>/', GetSingleMedicine.as_view({'list': 'get'})),
    path('cart/', CartView.as_view()),
    path('checkout/', OrderView.as_view()),
]
