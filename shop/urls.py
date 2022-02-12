from django.urls import path
from .views import MedicineView, TypeMedicineView, GetMedicineWithType

urlpatterns = [
    path('types/', TypeMedicineView.as_view()),
    path('medicines/', MedicineView.as_view()),
    path('medicines/<int:pk>/', GetMedicineWithType.as_view()),
]
