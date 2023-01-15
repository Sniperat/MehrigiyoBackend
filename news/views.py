from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from config.responses import ResponseSuccess, ResponseFail
from config.settings import FIREBASE_REGISTRATION_KEYS
from .serializers import NewsModelSerializer, TagsSerializer, AdvertisingSerializer, NotificationSerializer
from .models import NewsModel, TagsModel, Advertising, Notification
from .filters import NewsFilter
from .send_notification import sendPush
from account.models import UserModel
from .tasks import send_notification_func


class NewsView(generics.ListAPIView):
    queryset = NewsModel.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = NewsModelSerializer
    filterset_class = NewsFilter

    @swagger_auto_schema(
        operation_id='advertising',
        operation_description="advertisingView",
        # request_body=AdvertisingSerializer(),
        responses={
            '200': NewsModelSerializer()
        },
        manual_parameters=[
            openapi.Parameter('tag_id', openapi.IN_QUERY, description="test manual params",
                              type=openapi.TYPE_STRING)
        ],
    )
    def get(self, request, *args, **kwargs):
        key = request.GET.get('tag_id', False)
        if key:
            keys = key.split(',')
            self.queryset = NewsModel.objects.filter(hashtag_id__id__in=keys)
        return self.list(request, *args, **kwargs)
    # def get(self, request):
    #     filtered_qs = self.filterset_class(request.GET, queryset=self.get_queryset()).qs
    #
    #     page = self.paginate_queryset(filtered_qs)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return ResponseSuccess(data=self.get_paginated_response(serializer.data), request=request.method)


class TagView(APIView):
    queryset = TagsModel.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = TagsSerializer

    @swagger_auto_schema(
        operation_id='tags',
        operation_description="get tags",
        # request_body=TagsSerializer(),
        responses={
            '200': TagsSerializer()
        },
        manual_parameters=[
            openapi.Parameter('limit', openapi.IN_QUERY, description="Number of results to return per page.",
                              type=openapi.TYPE_NUMBER)
        ],
    )
    def get(self, request):
        key = request.GET.get('limit', False)
        asd = TagsModel.objects.all()
        if key:
            asd = TagsModel.objects.all()[:int(key)]
        serializer = TagsSerializer(asd, many=True)
        return Response(data=serializer.data)
    # def get(self, request, *args, **kwargs):

        # return self.list(request, *args, **kwargs)

    # @swagger_auto_schema(
    #     operation_id='tags',
    #     operation_description="post tags",
    #     request_body=InputSerializer(),
    #     responses={
    #         '200': TagsWithNewsSerializer()
    #     },
    # )
    # def post(self, request, *args, **kwargs):
    #     self.queryset = TagsModel.objects.filter(tag_name=request.data['tag'])
    #     return self.list(request, *args, **kwargs)


class AdvertisingShopView(generics.ListAPIView):
    queryset = Advertising.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = AdvertisingSerializer
    # pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    @swagger_auto_schema(
        operation_id='advertising',
        operation_description="advertisingView",
        # request_body=AdvertisingSerializer(),
        responses={
            '200': AdvertisingSerializer()
        },
    )
    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NotificationView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated,)


    @swagger_auto_schema(
        operation_id='notification',
        operation_description="get notifications",
        # request_body=NotificationSerializer(),
        responses={
            '200': NotificationSerializer()
        },)
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

            
        # else:
        #     for response in res.responses:
        #         if response.exception:
        #             response_index = res.responses.index(response)
        #             if response_index == 0:
        #                 error_device = 'Android'
        #             else:
        #                 error_device = 'IOS'
                    
        #             return Response(data={'message': f'failed for {error_device}. Exception: {response.exception}'})
                    

class NotificationCallView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_id='call_notification',
        operation_description="post Call notifications",
        # request_body=NotificationSerializer(),
        responses={
            '200': NotificationSerializer()
        },
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_QUERY, description="Send USer Id",
                              type=openapi.TYPE_NUMBER)
        ],
    )
    def post(self, request):
        pk = request.GET.get('pk', False)
        user = UserModel.objects.get(id=pk)
        current_user = request.user

        # sending to firebase
        image_path = None
        try:
            current_user.avatar.path
        except:
            pass

        res = sendPush(title='CALL', description=current_user.get_full_name(),
                       registration_tokens=[user.notificationKey],
                       image=image_path)
        success_count = res.success_count

        if success_count == 0:
            return Response(data={'message': f'failed. Exceptions:'
                                        f'{res.responses[0].exception}'})
            # notification.save()
        return Response(data={'message': f'success!'})

        # if success_count == 2:
        #     return Response({'message': f'success!'})
        # elif success_count == 0:
        #     return Response({'message': f'failed for both Android and IOS. Exceptions: Android: '
        #                                 f'{res.responses[0].exception}, IOS: {res.responses[1].exception}]'})
        # else:
        #     for response in res.responses:
        #         if response.exception:
        #             response_index = res.responses.index(response)
        #             if response_index == 0:
        #                 error_device = 'Android'
        #             else:
        #                 error_device = 'IOS'

        #             return Response({'message': f'failed for {error_device}. Exception: {response.exception}'})