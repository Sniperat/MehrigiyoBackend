from django.urls import path
from .views import NewsView, TagView, AdvertisingShopView

urlpatterns = [
    path('news/', NewsView.as_view()),
    path('tags/', TagView.as_view()),
    path('advertising/', AdvertisingShopView.as_view()),
]
