from django.urls import path, include
from .views import ChatView, MyChatsView

urlpatterns = [
    path('<int:pk>/', ChatView.as_view(), name='chat'),
    path('rooms/', MyChatsView.as_view(), name='chat'),

]
