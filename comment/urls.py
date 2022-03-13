from django.urls import path
from .views import CommentDoctorView, CommentMedicineView

urlpatterns = [
    path('doctor/<int:pk>/', CommentDoctorView.as_view()),
    path('medicine/<int:pk>/', CommentMedicineView.as_view()),

]
