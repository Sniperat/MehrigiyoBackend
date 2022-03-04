from django.urls import path
from .views import MedicinesView, TypeMedicineView, GetMedicinesWithType, GetSingleMedicine

urlpatterns = [
    path('types/', TypeMedicineView.as_view()),
    path('types/<int:pk>/', GetMedicinesWithType.as_view()),
    path('medicines/', MedicinesView.as_view()),
    path('medicines/<int:pk>/', GetSingleMedicine.as_view()),
]
