from channels.generic.websocket import WebsocketConsumer
from .serializers import MessageSerializer
from .models import ChatRoom, Message
from asgiref.sync import async_to_sync
import json


def getMessage(chat_id, user, msg):
    message = Message(**msg)
    message.owner = user
    message.save()
    room = ChatRoom.objects.get(id=chat_id)
    room.messages.add(message)
    room.save()
    serializer = MessageSerializer(message)

    return serializer.data


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'chat_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        chat_id = text_data_json['chat_id']
        msg = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'chat_id': chat_id,
                'message': msg

            }
        )

    def chat_message(self, event):
        chat_id = event['chat_id']
        current_user = self.scope["user"]
        msg = event['message']
        data = getMessage(chat_id, current_user, msg)
        self.send(text_data=json.dumps({
            "status": "success",
            "data": data,
        }))
