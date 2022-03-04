from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from config.responses import ResponseSuccess, ResponseFail
from shop.models import Medicine
from specialist.models import Doctor
from .models import CommentDoctor, CommentMedicine
from .serializers import CommentDoctorSerializer, CommentMedicineSerializer


class CommentDoctorView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        comment = CommentDoctor.objects.filter(doctor_id=pk)
        serializer = CommentDoctorSerializer(comment, many=True)
        return ResponseSuccess(data=serializer.data, request=request.method)

    def post(self, request, pk):
        doctor = Doctor.objects.get(doctor_id=pk)
        serializer = CommentDoctorSerializer(data=request.data)
        if serializer.is_valid():
            comment = CommentDoctor(**serializer.data)
            comment.user = request.user
            comment.medicine = doctor
            comment.save()
            s = CommentDoctorSerializer(comment)
            return ResponseSuccess(data=s.data, request=request.method)
        return ResponseFail(data=serializer.errors, request=request.method)


class CommentMedicineView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        comment = CommentMedicine.objects.filter(medicine_id=pk)
        serializer = CommentMedicineSerializer(comment, many=True)
        return ResponseSuccess(data=serializer.data, request=request.method)

    def post(self, request, pk):
        medicine = Medicine.objects.get(medicine_id=pk)
        serializer = CommentMedicineSerializer(data=request.data)
        if serializer.is_valid():
            comment = CommentMedicine(**serializer.data)
            comment.user = request.user
            comment.medicine = medicine
            comment.save()
            s = CommentMedicineSerializer(comment)
            return ResponseSuccess(data=s.data, request=request.method)
        return ResponseFail(data=serializer.errors, request=request.method)





