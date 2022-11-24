from rest_framework import serializers
from .models import ChatRoom, Message, FileMessage
from account.models import UserModel
from specialist.models import AdviceTime
from specialist.serializers import AdviceSerializer
import datetime


class ChatSerializer(serializers.ModelSerializer):
    # messages = MessageSerializer(many=True)

    class Meta:
        model = ChatRoom
        fields = ['id', 'get_doctor_fullname', 'get_client_fullname','token', 'created_at']


class FileMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileMessage
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    file_message = FileMessageSerializer()

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


class RoomsSerializer(serializers.ModelSerializer):
    last_message = MessageSerializer()
    doktor = serializers.SerializerMethodField(method_name='get_doctor')
    client = serializers.SerializerMethodField(method_name='get_cname')
    advice_time = serializers.SerializerMethodField(method_name="get_advice")

    def get_advice(self, obj):
        ad = AdviceTime.objects.filter(doctor=obj.doktor.specialist_doctor,
                                    client=obj.client,
                                    start_time__gte=datetime.datetime.now()).first()
        if ad != None:
            ser = AdviceSerializer(ad)
            return ser.data
        else:
            return ''

    def get_doctor(self, obj):
        imma = obj.doktor.specialist_doctor.image.url
        if imma != '':
            return {
                "doctor_account_id": obj.doktor.id,
                "specialist_account_id": obj.doktor.specialist_doctor.id,
                "name": obj.doktor.get_full_name(),
                "image": imma,
                "type": obj.doktor.specialist_doctor.type_doctor.name
            }
        else:
             return {
                "doctor_account_id": obj.doktor.id,
                "specialist_account_id": obj.doktor.specialist_doctor.id,
                "name": obj.doktor.get_full_name(),
                "type": obj.doktor.specialist_doctor.type_doctor.name
            }
   
    def get_cname(self, obj):
        return obj.client.get_full_name()

    class Meta:
        model = ChatRoom
        fields = ('id', 'client', 'doktor', 'last_message', 'advice_time','token', 'created_at')

