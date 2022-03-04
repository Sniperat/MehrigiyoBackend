from django.shortcuts import render
from account.models import UserModel
from .models import ChatRoom
from .serializers import ChatSerializer, RoomsSerializer
from specialist.models import Doctor
from rest_framework.views import APIView
from config.responses import ResponseFail, ResponseSuccess


class ChatView(APIView):
    def get(self, request, pk):
        doctor = Doctor.objects.get(id=pk)
        user = UserModel.objects.get(specialist_doctor=doctor, is_staff=True)

        try:
            room = ChatRoom.objects.get(client=request.user, doktor=user)
        except:
            room = None
        if room is None:
            room = ChatRoom()
            room.client = request.user
            room.doktor = user
            room.save()

        serializer = ChatSerializer(room)
        return ResponseSuccess(data=serializer.data, request=request.method)


class MyChatsView(APIView):
    def get(self, request):

        rooms = ChatRoom.objects.filter(client=request.user)
        serializer = RoomsSerializer(rooms, many=True)
        return ResponseSuccess(data=serializer.data, request=request.method)

