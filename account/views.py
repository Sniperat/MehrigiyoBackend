from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserModel, CountyModel, RegionModel, DeliveryAddress
from shop.models import Medicine
from specialist.models import Doctor
from config.helpers import send_sms_code, validate_sms_code
from config.validators import PhoneValidator
from config.responses import ResponseFail, ResponseSuccess
from .serializers import (SmsSerializer, ConfirmSmsSerializer, RegistrationSerializer,
                          RegionSerializer, CountrySerializer, UserSerializer, DeliverAddressSerializer)


class SendSmsView(APIView):
    def get(self, request):
        serializer = SmsSerializer()
        return ResponseSuccess(data=serializer.data, request=request.method)

    def post(self, request):
        serializer = SmsSerializer(data=request.data)
        if serializer.is_valid():
            send_sms_code(request, serializer.data['phone'])
            return ResponseSuccess(request=request.method)
        return ResponseFail(data=serializer.errors, request=request.method)


class ConfirmSmsView(APIView):

    def get(self, request):
        serializer = ConfirmSmsSerializer()
        return ResponseSuccess(data=serializer.data, request=request.method)

    def post(self, request):
        serializer = ConfirmSmsSerializer(data=request.data)
        if serializer.is_valid():
            if validate_sms_code(serializer.data['phone'], serializer.data['code']):
                return ResponseSuccess(data="Telefon nomer tasdiqladi", request=request.method)
            else:
                return ResponseFail(data='Code hato kiritilgan', request=request.method)
        return ResponseFail(data=serializer.errors, request=request.method)


class RegistrationView(APIView):

    def get(self, request):
        serializer = RegistrationSerializer()
        return ResponseSuccess(data=serializer.data, request=request.method)

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseSuccess(data=serializer.data, request=request.method)
        else:
            return ResponseFail(data=serializer.errors, request=request.method)


class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return ResponseSuccess(data=serializer.data, request=request.method)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseSuccess(data=serializer.data, request=request.method)
        else:
            return ResponseFail(data=serializer.errors, request=request.method)


class RegionView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        reg = RegionModel.objects.all()
        serializer = RegionSerializer(reg, many=True)
        return ResponseSuccess(data=serializer.data, request=request.method)


class CountryView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        coun = CountyModel.objects.all()
        serializer = CountrySerializer(coun, many=True)
        return ResponseSuccess(data=serializer.data, request=request.method)


class AddAddressView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            id = request.data['region_id']
        except:
            return ResponseFail(data='Bunday Viloyat mavjud emas', request=request.method)
        region = RegionModel.objects.get(id=id)
        user = request.user
        user.address = region
        user.save()
        return ResponseSuccess(request=request.method)


class MedicineView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        try:
            med = Medicine.objects.get(id=pk)
        except:
            return ResponseFail(data='Bunday dori mavjud emas', request=request.method)
        user = request.user
        user.favorite_medicine.add(med)
        user.save()
        return ResponseSuccess(request=request.method)

    def delete(self, request, pk):
        try:
            med = Medicine.objects.get(id=pk)
        except:
            return ResponseFail(data='Bunday dori mavjud emas', request=request.method)
        user = request.user
        user.favorite_medicine.remove(med)
        user.save()
        return ResponseSuccess(request=request.method)


class DoctorView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        try:
            doc = Doctor.objects.get(id=pk)
        except:
            return ResponseFail(data='Bunday doktr mavjud emas', request=request.method)
        user = request.user
        user.favorite_doctor.add(doc)
        user.save()
        return ResponseSuccess(request=request.method)

    def delete(self, request, pk):
        try:
            doc = Doctor.objects.get(id=pk)
        except:
            return ResponseFail(data='Bunday doktor mavjud emas', request=request.method)
        user = request.user
        user.favorite_doctor.remove(doc)
        user.save()
        return ResponseSuccess(request=request.method)


class DeliverAddressView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        address = DeliveryAddress.objects.filter(user=request.user)
        serializers = DeliverAddressSerializer(address, many=True)
        return ResponseSuccess(data=serializers.data, request=request.method)

    def post(self, request):
        serializers = DeliverAddressSerializer(data=request.data)

        if serializers.is_valid():
            da = DeliveryAddress(**serializers.data)
            da.user = request.user
            da.save()
            return ResponseSuccess(data=serializers.data, request=request.method)
        else:
            return ResponseFail(data=serializers.errors, request=request.method)


