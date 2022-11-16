from channels.db import database_sync_to_async
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from .serializers import MessageSerializer
from .models import ChatRoom, Message, FileMessage
from asgiref.sync import async_to_sync
import json


def getMessage(chat_id, user, msg):
    try:
        f =FileMessage.objects.get(id=msg['file_message'])
        del msg['file_message']
    except:
        f = None
    message = Message(**msg)
    message.owner = user
    message.file_message = f
    message.save()
    room = ChatRoom.objects.get(id=chat_id)
    room.messages.add(message)
    room.save()
    serializer = MessageSerializer(message)


    return serializer.data

@database_sync_to_async
def createVideoChat(chat_id, user):
    message = Message(video=True)
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
        current_user = self.scope["user"]
        print(current_user, '==========')
        data = getMessage(chat_id, current_user, msg)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'data': data

            }
        )

    def chat_message(self, event):
        data = event['data']
        self.send(text_data=json.dumps({
            "status": "success",
            "data": data,
        }))


class VideoChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        receive_dict = json.loads(text_data)
        message = receive_dict['message']
        action = receive_dict['action']

        if (action == 'new-offer') or (action == 'new-answer'):
            receiver_channel_name = receive_dict['message']['receiver_channel_name']

            receive_dict['message']['receiver_channel_name'] = self.channel_name

            await self.channel_layer.send(
                receiver_channel_name,
                {
                    'type': 'send.sdp',
                    'receive_dict': receive_dict
                }
            )

            return

        receive_dict['message']['receiver_channel_name'] = self.channel_name

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send.sdp',
                'receive_dict': receive_dict
            }
        )

    async def send_sdp(self, event):
        receive_dict = event['receive_dict']
        chat_id = self.room_name
        current_user = self.scope["user"]
        # data = await createVideoChat(chat_id, current_user)
        # print(data)
        await self.send(text_data=json.dumps(receive_dict))


