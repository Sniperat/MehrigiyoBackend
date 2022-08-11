from rest_framework import serializers
from .models import ChatRoom, Message
from account.models import UserModel

class MessageSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user = representation['owner']
        u = UserModel.objects.get(id=user)
        print(user)
        if u.is_staff:
            representation['doctor'] = True
        representation['doctor'] = False
        return representation

    class Meta:
        model = Message
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    # messages = MessageSerializer(many=True)

    class Meta:
        model = ChatRoom
        fields = ['id', 'get_doctor_fullname', 'get_client_fullname', 'created_at']


class RoomsSerializer(serializers.ModelSerializer):
    last_message = MessageSerializer()

    class Meta:
        model = ChatRoom
        fields = ('id', 'client', 'doktor', 'last_message', 'created_at')
