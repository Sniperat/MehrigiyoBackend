from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from config.responses import ResponseSuccess, ResponseFail
from .serializers import TypeDoctorSerializer, DoctorSerializer
from .models import Doctor, TypeDoctor


class TypeDoctorView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        types = TypeDoctor.objects.all()
        serializer = TypeDoctorSerializer(types, many=True)
        return ResponseSuccess(data=serializer.data, request=request.method)


class DoctorsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        medicine = Doctor.objects.all()
        serializer = DoctorSerializer(medicine, many=True)
        return ResponseSuccess(data=serializer.data, request=request.method)


class GetDoctorsWithType(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        medicine = Doctor.objects.filter(type_doctor_id=pk)
        serializer = DoctorSerializer(medicine, many=True)
        return ResponseSuccess(data=serializer.data, request=request.method)


class GetSingleDoctor(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        doc = Doctor.objects.get(id=pk)
        serializer = DoctorSerializer(doc)
        return ResponseSuccess(data=serializer.data, request=request.method)

