import random
import string

from django.db import models
from account.models import UserModel
import datetime

today = datetime.date.today()


class Message(models.Model):
    owner = models.ForeignKey(UserModel, on_delete=models.RESTRICT)
    text = models.CharField(max_length=255, null=True, blank=True)
    file_message = models.ForeignKey('FileMessage', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class FileMessage(models.Model):
    image = models.ImageField(upload_to=f'message/images/{today.year}-{today.month}-{today.month}/',

                              null=True, blank=True)
    file = models.FileField(upload_to=f'message/files/{today.year}-{today.month}-{today.month}/',
                            null=True, blank=True)
    size = models.CharField(max_length=50, null=True, blank=True)
    video = models.BooleanField(default=False)

class ChatRoom(models.Model):
    admin = models.ForeignKey(UserModel, on_delete=models.RESTRICT, related_name='chat_admin', null=True, blank=True)
    client = models.ForeignKey(UserModel, on_delete=models.RESTRICT, related_name='chat_client', null=True, blank=True)
    doktor = models.ForeignKey(UserModel, on_delete=models.RESTRICT, related_name='chat_doctor')
    messages = models.ManyToManyField(Message, related_name='words')
    token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def last_message(self):
        return self.messages.last()

    def get_doctor_fullname(self):
        return self.doktor.get_full_name()

    def get_client_fullname(self):
        return self.client.get_full_name()
