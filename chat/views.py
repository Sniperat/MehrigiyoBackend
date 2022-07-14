from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from account.models import UserModel
from .models import ChatRoom
from .serializers import ChatSerializer, RoomsSerializer
from specialist.models import Doctor
from rest_framework.views import APIView
from config.responses import ResponseFail, ResponseSuccess


class ChatView(APIView):
    @swagger_auto_schema(
        # request_body=DoctorSerializer(),
        responses={
            '200': ChatSerializer()
        },
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_QUERY, description="doctor_id",
                              type=openapi.TYPE_NUMBER)
        ], operation_description='GET News')
    @action(detail=False, methods=['get'])
    def get(self, request):
        key = request.GET.get('pk', False)
        if key:
            doctor = Doctor.objects.get(id=key)
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
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_id='chat_view',
        operation_description="chat_view",
        # request_body=RoomsSerializer(),
        responses={
            '200': RoomsSerializer()
        },
    )
    def get(self, request):

        rooms = ChatRoom.objects.filter(client=request.user)
        serializer = RoomsSerializer(rooms, many=True)
        return ResponseSuccess(data=serializer.data, request=request.method)

