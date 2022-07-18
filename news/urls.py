from django.urls import path
from .views import NewsView, TagView

urlpatterns = [
    path('news/', NewsView.as_view()),
    path('tags/', TagView.as_view())
]
