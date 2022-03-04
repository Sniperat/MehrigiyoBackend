from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from config.responses import ResponseSuccess, ResponseFail
from .serializers import TypeMedicineSerializer, MedicineSerializer
from .models import PicturesMedicine, TypeMedicine, Medicine


class TypeMedicineView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        types = TypeMedicine.objects.all()
        serializer = TypeMedicineSerializer(types, many=True)
        return ResponseSuccess(data=serializer.data, request=request.method)


class MedicinesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        medicine = Medicine.objects.all()
        serializer = MedicineSerializer(medicine, many=True)
        return ResponseSuccess(data=serializer.data, request=request.method)


class GetMedicinesWithType(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        medicine = Medicine.objects.filter(type_medicine_id=pk)
        serializer = MedicineSerializer(medicine, many=True)
        return ResponseSuccess(data=serializer.data, request=request.method)


class GetSingleMedicine(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        medicine = Medicine.objects.get(id=pk)
        serializer = MedicineSerializer(medicine)
        return ResponseSuccess(data=serializer.data, request=request.method)


