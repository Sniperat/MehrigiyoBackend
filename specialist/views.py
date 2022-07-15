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
from .serializers import TypeDoctorSerializer, DoctorSerializer, RateSerializer, AdvertisingSerializer
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


class TypeDoctorView(viewsets.mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = TypeDoctor.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = TypeDoctorSerializer

    @swagger_auto_schema(
        operation_id='get_doctor_types',
        operation_description="get_doctor_types",
        request_body=TypeDoctorSerializer(),
        responses={
            '200': TypeDoctorSerializer()
        },
        # method='get'
        # permission_classes=[IsAuthenticated, ],
        # tags=['photos'],
    )
    # @api_view(['GET'])
    # @action(detail=True, methods=['get'])
    def get(self, request):

        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return ResponseSuccess(data=self.get_paginated_response(serializer.data), request=request.method)


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
        # method='get'
        # permission_classes=[IsAuthenticated, ],
        # tags=['photos'],
    )
    def get(self, request, *args, **kwargs):
        queryset = self.queryset.annotate(
            total_rate=Avg('comments_doc__rate')
        )
        filtered_qs = self.filterset_class(request.GET, queryset=queryset).qs
        self.queryset = filtered_qs
        print('333333333333')

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
