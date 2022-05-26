from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

import datetime
import pytz

from config.responses import ResponseSuccess, ResponseFail
from .serializers import TypeDoctorSerializer, DoctorSerializer, RateSerializer
from .models import Doctor, TypeDoctor, AdviceTime

utc = pytz.UTC


class TypeDoctorView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        types = TypeDoctor.objects.all()
        serializer = TypeDoctorSerializer(types, many=True)
        return ResponseSuccess(data=serializer.data, request=request.method)


class DoctorsView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        medicine = Doctor.objects.all()
        serializer = DoctorSerializer(medicine, many=True)
        return ResponseSuccess(data=serializer.data, request=request.method)


class GetDoctorsWithType(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        medicine = Doctor.objects.filter(type_doctor_id=pk)
        serializer = DoctorSerializer(medicine, many=True)
        return ResponseSuccess(data=serializer.data, request=request.method)


class GetSingleDoctor(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        doc = Doctor.objects.get(id=pk)
        doc.review = doc.review + 1
        serializer = DoctorSerializer(doc)
        return ResponseSuccess(data=serializer.data, request=request.method)


class RateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = RateSerializer(data=request.data,
                                    context={'request': request},
                                    required=False)

        if serializer.is_valid():
            serializer.save()
            return ResponseSuccess(data=serializer.data)
        else:
            return ResponseFail(data=serializer.errors)


class AdviceView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        advice = AdviceTime.objects.filter(doctor_id=pk)
        data_now = datetime.datetime.now()
        data_times = []
        for i in advice:
            # if i.start_time >= data_now:
            data_times.append(i.start_time)
        return ResponseSuccess(data=data_times)

    def post(self, request, pk):
        date_time_input = request.data['datatime']

        date_time_obj = datetime.datetime.strptime(date_time_input, '%d/%m/%y %H:%M:%S')

        advice = None
        try:
            advice = AdviceTime.objects.get(start_time=date_time_obj)
        except:
            pass
        if advice is not None:
            return ResponseFail(data='this time is busy')
        advice = AdviceTime()
        advice.client = request.user
        advice.doctor = Doctor.objects.get(id=pk)
        advice.start_time = date_time_obj
        advice.save()
        return ResponseSuccess()
