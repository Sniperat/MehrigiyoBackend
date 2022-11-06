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
        fields = ['id', 'get_doctor_fullname', 'get_client_fullname','token', 'created_at']


class RoomsSerializer(serializers.ModelSerializer):
    last_message = MessageSerializer()
    doktor = serializers.SerializerMethodField(method_name='get_name')
    client = serializers.SerializerMethodField(method_name='get_cname')

    def get_name(self, obj):
        return obj.doktor.get_full_name()

    def get_cname(self, obj):
        return obj.client.get_full_name()

    class Meta:
        model = ChatRoom
        fields = ('id', 'client', 'doktor', 'last_message','token', 'created_at')
