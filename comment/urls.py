from django.urls import path
from .views import CommentDoctorView, CommentMedicineView

urlpatterns = [
    path('doctors/<int:pk>/', CommentDoctorView.as_view()),
    path('medicines/<int:pk>/', CommentMedicineView.as_view()),

]
