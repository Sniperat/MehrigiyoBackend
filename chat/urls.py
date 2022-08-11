from django.urls import path, include
from .views import ChatView, MyChatsView, MessageView

urlpatterns = [
    path('', ChatView.as_view(), name='chat'),
    path('messages/', MessageView.as_view(), name='chat'),
    path('rooms/', MyChatsView.as_view(), name='chat'),

]
