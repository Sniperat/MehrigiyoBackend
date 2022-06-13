from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from account.models import UserModel, SmsCode, SmsAttempt, CountyModel, RegionModel, DeliveryAddress
from chat.models import Message, ChatRoom
from comment.models import CommentDoctor, CommentMedicine
from news.models import NewsModel
from paymeuz.models import PaymeTransactionModel, Card
from shop.models import PicturesMedicine, TypeMedicine, Medicine, CartModel, DeliveryMan, OrderModel
from specialist.models import TypeDoctor, Doctor, RateDoctor, AdviceTime


class UserModelAdminViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelAdminSerializer
    permission_classes = [IsAuthenticated, ]


class SmsCodeAdminViewSet(viewsets.ModelViewSet):
    queryset = SmsCode.objects.all()
    serializer_class = SmsCodeAdminSerializer
    permission_classes = [IsAuthenticated, ]


class SmsAttemptAdminViewSet(viewsets.ModelViewSet):
    queryset = SmsAttempt.objects.all()
    serializer_class = SmsAttemptAdminSerializer
    permission_classes = [IsAuthenticated, ]


class CountyModelAdminViewSet(viewsets.ModelViewSet):
    queryset = CountyModel.objects.all()
    serializer_class = CountryModelAdminSerializer
    permission_classes = [IsAuthenticated, ]


class RegionModelAdminViewSet(viewsets.ModelViewSet):
    queryset = RegionModel.objects.all()
    serializer_class = RegionModelAdminSerializer
    permission_classes = [IsAuthenticated, ]


class DeliveryAddressAdminViewSet(viewsets.ModelViewSet):
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressAdminSerializer
    permission_classes = [IsAuthenticated, ]


class MessageAdminViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageAdminSerializer
    permission_classes = [IsAuthenticated, ]


class ChatRoomAdminViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomAdminSerializer
    permission_classes = [IsAuthenticated, ]


class CommentDoctorAdminViewSet(viewsets.ModelViewSet):
    queryset = CommentDoctor.objects.all()
    serializer_class = CommentDoctorAdminSerializer
    permission_classes = [IsAuthenticated, ]


class CommentMedicineAdminViewSet(viewsets.ModelViewSet):
    queryset = CommentMedicine.objects.all()
    serializer_class = CommentMedicineAdminSerializer
    permission_classes = [IsAuthenticated, ]


class NewsModelAdminViewSet(viewsets.ModelViewSet):
    queryset = NewsModel.objects.all()
    serializer_class = NewsModelAdminSerializer
    permission_classes = [IsAuthenticated, ]


class PaymeTransactionModelAdminViewSet(viewsets.ModelViewSet):
    queryset = PaymeTransactionModel.objects.all()
    serializer_class = PaymeTransactionModelAdminSerializer
    permission_classes = [IsAuthenticated, ]


class CardAdminViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardAdminSerializer
    permission_classes = [IsAuthenticated, ]


class PicturesMedicineAdminViewSet(viewsets.ModelViewSet):
    queryset = PicturesMedicine.objects.all()
    serializer_class = PicturesMedicineAdminSerializer
    permission_classes = [IsAuthenticated, ]


class TypeMedicineAdminViewSet(viewsets.ModelViewSet):
    queryset = TypeMedicine.objects.all()
    serializer_class = TypeMedicineAdminSerializer
    permission_classes = [IsAuthenticated, ]


class MedicineAdminViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineAdminSerializer
    permission_classes = [IsAuthenticated, ]


class CartModelAdminViewSet(viewsets.ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = CartModelAdminSerializer
    permission_classes = [IsAuthenticated, ]


class DeliveryManAdminViewSet(viewsets.ModelViewSet):
    queryset = DeliveryMan.objects.all()
    serializer_class = DeliveryManAdminSerializer
    permission_classes = [IsAuthenticated, ]


class OrderModelAdminViewSet(viewsets.ModelViewSet):
    queryset = OrderModel.objects.all()
    serializer_class = OrderModelAdminSerializer
    permission_classes = [IsAuthenticated, ]


class TypeDoctorAdminViewSet(viewsets.ModelViewSet):
    queryset = TypeDoctor.objects.all()
    serializer_class = TypeDoctorAdminSerializer
    permission_classes = [IsAuthenticated, ]


class DoctorAdminViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorAdminSerializer
    permission_classes = [IsAuthenticated, ]


class RateDoctorAdminViewSet(viewsets.ModelViewSet):
    queryset = RateDoctor.objects.all()
    serializer_class = RateDoctorAdminSerializer
    permission_classes = [IsAuthenticated, ]


class AdviceTimeAdminViewSet(viewsets.ModelViewSet):
    queryset = AdviceTime.objects.all()
    serializer_class = AdviceTimeAdminSerializer
    permission_classes = [IsAuthenticated, ]
