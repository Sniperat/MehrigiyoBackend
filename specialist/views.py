from django.db.models import Sum, Avg
from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework import generics

import datetime
import pytz

from config.responses import ResponseSuccess, ResponseFail
from .serializers import TypeDoctorSerializer, DoctorSerializer, RateSerializer, AdvertisingSerializer, AdviceSerializer
from .models import Doctor, TypeDoctor, AdviceTime, Advertising
from .filters import DoctorFilter

utc = pytz.UTC


class AdvertisingView(generics.ListAPIView):
    queryset = Advertising.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = AdvertisingSerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    @swagger_auto_schema(
        operation_id='advertising',
        operation_description="advertisingView",
        # request_body=AdvertisingSerializer(),
        responses={
            '200': AdvertisingSerializer()
        },
    )
    def get(self, request, *args, **kwargs):

        return self.list(request, *args, **kwargs)


class TypeDoctorView(generics.ListAPIView):
    queryset = TypeDoctor.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = TypeDoctorSerializer

    @swagger_auto_schema(
        operation_id='get_doctor_types',
        operation_description="get_doctor_types",
        # request_body=TypeDoctorSerializer(),
        responses={
            '200': TypeDoctorSerializer()
        },

    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class DoctorsView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = DoctorSerializer
    filterset_class = DoctorFilter

    @swagger_auto_schema(
        operation_id='get_doctors',
        operation_description="get_doctors",
        # request_body=DoctorSerializer(),
        responses={
            '200': DoctorSerializer()
        },
        manual_parameters=[
            openapi.Parameter('type_ides', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_STRING)
        ]
    )
    def get(self, request, *args, **kwargs):
        key = request.GET.get('type_ides', False)
        queryset = self.queryset.annotate(
            total_rate=Avg('comments_doc__rate')
        ).order_by('-total_rate')
        filtered_qs = self.filterset_class(request.GET, queryset=queryset).qs
        for i in filtered_qs:
            i.review = i.review + 1
            i.save()
        self.queryset = filtered_qs
        if key:
            keys = key.split(',')
            self.queryset = self.queryset.filter(type_doctor_id__in=keys)
        return self.list(request, *args, **kwargs)

    def get_serializer_context(self):
        context = super(DoctorsView, self).get_serializer_context()
        context.update({'user': self.request.user})
        return context


class GetDoctorsWithType(generics.ListAPIView):
    queryset = Doctor.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = DoctorSerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    @swagger_auto_schema(
        # request_body=DoctorSerializer(),
        manual_parameters=[
        openapi.Parameter('type_ides', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_STRING)
    ], operation_description='GET /articles/today/')
    @action(detail=False, methods=['get'])
    def get(self, request, *args, **kwargs):
        key = request.GET.get('type_ides', False)
        print('rabotaet')
        if key:
            print('rabotaet')
            keys = key.split(',')
            print(keys, '---------------')
            self.queryset = self.queryset.filter(type_doctor_id__in=keys)
            print('333333333333')
        return self.list(request, *args, **kwargs)


class GetSingleDoctor(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = DoctorSerializer

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('pk', openapi.IN_QUERY, description="test manual param", type=openapi.TYPE_NUMBER)
    ])
    def get(self, request):
        key = request.GET.get('pk', False)
        from django.db.models import Avg
        queryset = self.queryset.annotate(
            total_rate=Avg('comments_doc__rate')
        )

        if key:
            queryset = Doctor.objects.get(id=key)
            queryset.review = queryset.review + 1
            queryset.save()
        serializer = self.get_serializer(queryset, context={'user': request.user})

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

    @swagger_auto_schema(
        operation_id='get_advice_times',
        operation_description="get_advice_times",
        # request_body=DoctorSerializer(),
        responses={
            '200': AdviceSerializer()
        },
        manual_parameters=[
            openapi.Parameter('day', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
            openapi.Parameter('month', openapi.IN_QUERY,  type=openapi.TYPE_INTEGER),
            openapi.Parameter('year', openapi.IN_QUERY, type=openapi.TYPE_INTEGER),

            openapi.Parameter('my', openapi.IN_QUERY, description="all clients time", type=openapi.TYPE_BOOLEAN)
        ]
    )
    def get(self, request, pk):
        day = request.GET.get('day', False)
        month = request.GET.get('month', False)
        year = request.GET.get('year', False)
        my = request.GET.get('my', False)

        if my:
            advice = AdviceTime.objects.filter(doctor_id=pk,
                                               client=request.user,
                                               start_time__day=day,
                                               start_time__month=month,
                                               start_time__year=year)
        else:
            advice = AdviceTime.objects.filter(doctor_id=pk,
                                               start_time__day=day,
                                               start_time__month=month,
                                               start_time__year=year)

        ser = AdviceSerializer(advice, many=True)
        return ResponseSuccess(data=ser.data)

    def post(self, request, pk):
        date_time_start = request.data['start_time']
        date_time_end = request.data['end_time']

        date_time_start_obj = datetime.datetime.strptime(date_time_start, '%d/%m/%y %H:%M:%S')
        date_time_end_obj = datetime.datetime.strptime(date_time_end, '%d/%m/%y %H:%M:%S')

        advice = None
        try:
            advice = AdviceTime.objects.get(start_time=date_time_start_obj, end_time=date_time_end_obj)
        except:
            pass
        if advice is not None:
            return ResponseFail(data='this time is busy')
        advice = AdviceTime()
        advice.client = request.user
        advice.doctor = Doctor.objects.get(id=pk)
        advice.start_time = date_time_start_obj
        advice.end_time = date_time_end_obj
        advice.save()
        return ResponseSuccess()
