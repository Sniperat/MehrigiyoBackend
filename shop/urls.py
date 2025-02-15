from django.urls import path, include, re_path
from rest_framework import routers

from .views import (MedicinesView, TypeMedicineView, GetMedicinesWithType, MedicineRetrieveView, CartView,
                    OrderView, SearchView)
router = routers.DefaultRouter()
router.register(r'types', TypeMedicineView)

urlpatterns = [
    path('', include(router.urls)),

    # path('types/', TypeMedicineView.as_view()),
    # path('types/one/', GetMedicinesWithType.as_view()),
    path('medicines/', MedicinesView.as_view()),
    path('medicines/<int:pk>/', MedicineRetrieveView.as_view()),
    path('cart/', CartView.as_view()),
    path('checkout/', OrderView.as_view()),

    path('search/', SearchView.as_view(), name='search'),

]
