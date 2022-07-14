from django.urls import path
from .views import CommentDoctorView, CommentMedicineView

urlpatterns = [
    path('doctor/', CommentDoctorView.as_view()),
    path('medicine/', CommentMedicineView.as_view()),

]
