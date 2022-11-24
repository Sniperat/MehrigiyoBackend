import datetime
import random
import string

from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from account.models import UserModel, OfferModel
from account.serializers import OfferSerializer
from .models import ChatRoom, Message, FileMessage
from .serializers import ChatSerializer, RoomsSerializer, MessageSerializer, FileMessageSerializer
from specialist.models import Doctor, AdviceTime
from rest_framework.views import APIView
from config.responses import ResponseFail, ResponseSuccess


class ChatView(APIView):
    @swagger_auto_schema(
        # request_body=DoctorSerializer(),
        responses={
            '200': ChatSerializer()
        },
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_QUERY, description="pk",
                              type=openapi.TYPE_NUMBER),
            openapi.Parameter('admin', openapi.IN_QUERY, description="chat with admin",
                              type=openapi.TYPE_BOOLEAN)
        ], operation_description='GET News')
    @action(detail=False, methods=['get'])
    def get(self, request):
        key = request.GET.get('pk', False)
        admin = request.GET.get('admin', False)
        if admin:
            user = UserModel.objects.filter(is_superuser=True).first()
            try:
                room = ChatRoom.objects.get(client=request.user, admin=user)
            except:
                room = None
            if room is None:
                from uuid import uuid4
                rand_token = uuid4()
                room = ChatRoom()
                room.client = request.user
                room.admin = user
                room.token = rand_token
                room.save()

            serializer = ChatSerializer(room)
            return ResponseSuccess(data=serializer.data, request=request.method)
        if key:
            try:
                doctor = Doctor.objects.get(id=key)
            except:
                return ResponseFail(data='Doctor not Found')
            
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
        return ResponseFail(data="Tere is no key, no admin!")


class FileMessageView(APIView):
    # permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_id='file_mess',
        operation_description="File Message",
        responses={
            '200': FileMessageSerializer()
        },
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_QUERY, description="File ID",
                              type=openapi.TYPE_NUMBER),
        ],
    )
    def get(self, request):
        key = request.GET.get('pk', False)
        if key:
            file = FileMessage.objects.get(id=key)
            serializer = FileMessageSerializer(file)
            return ResponseSuccess(serializer.data)
        return ResponseFail(data="File not found")
    
    @swagger_auto_schema(
        operation_id='file_mess_create',
        operation_description="File Message Create",
        request_body=FileMessageSerializer,
        responses={
            '200': FileMessageSerializer()
        },
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_QUERY, description="File ID",
                              type=openapi.TYPE_NUMBER),
        ],
    )
    def post(self, request):
        serializer = FileMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseSuccess(data=serializer.data)
        else:
            return ResponseFail(data=serializer.errors)


class MyChatsView(generics.ListAPIView):
    queryset = ChatRoom.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = RoomsSerializer

    @swagger_auto_schema(
        operation_id='chat_view',
        operation_description="chat_view",
        # request_body=RoomsSerializer(),
        responses={
            '200': RoomsSerializer()
        },
    )
    def get(self, request, *args, **kwargs):

        rooms = ChatRoom.objects.filter(client=request.user)
        # ad = AdviceTime.objects.filter(client=request.user, start_time__gte=datetime.datetime.now()).first()
        # print(ad)
        self.queryset = rooms
        # serializer = RoomsSerializer(rooms, many=True)
        return self.list(request, *args, **kwargs)



class MessageView(generics.ListAPIView):
    queryset = Message.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = MessageSerializer

    @swagger_auto_schema(
        # request_body=DoctorSerializer(),
        responses={
            '200': MessageSerializer()
        },
        manual_parameters=[
            openapi.Parameter('chat_id', openapi.IN_QUERY, description="chat_id",
                              type=openapi.TYPE_NUMBER)
        ], operation_description='get all messages with pagination')
    def get(self, request, *args, **kwargs):
        key = request.GET.get('chat_id', False)
        if key:
            chr = ChatRoom.objects.get(id=key)
            self.queryset = chr.messages.all().order_by('-id')
        return self.list(request, *args, **kwargs)
