from django.db import models
from account.models import UserModel
import datetime
today = datetime.date.today()


class Message(models.Model):
    owner = models.ForeignKey(UserModel, on_delete=models.RESTRICT)
    text = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to=f'message/images/{today.year}-{today.month}-{today.month}/',
                              null=True, blank=True)
    file = models.FileField(upload_to=f'message/files/{today.year}-{today.month}-{today.month}/',
                            null=True, blank=True)
    video = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class ChatRoom(models.Model):
    client = models.ForeignKey(UserModel, on_delete=models.RESTRICT, related_name='chat_client')
    doktor = models.ForeignKey(UserModel, on_delete=models.RESTRICT, related_name='chat_doctor')
    messages = models.ManyToManyField(Message, related_name='words')
    created_at = models.DateTimeField(auto_now_add=True)

    def last_message(self):
        return self.messages.last()
