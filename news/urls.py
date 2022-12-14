from django.urls import path
from .views import NewsView, TagView, AdvertisingShopView, NotificationView, NotificationCallView

urlpatterns = [
    path('', NewsView.as_view()),
    path('tags/', TagView.as_view()),
    path('advertising/', AdvertisingShopView.as_view()),
    path('notification/', NotificationView.as_view()),
    path('notification/call/', NotificationCallView.as_view())

]
