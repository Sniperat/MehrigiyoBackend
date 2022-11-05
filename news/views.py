from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from config.responses import ResponseSuccess, ResponseFail
from .serializers import NewsModelSerializer, TagsSerializer, AdvertisingSerializer, NotificationSerializer
from .models import NewsModel, TagsModel, Advertising, Notification
from .filters import NewsFilter


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
            openapi.Parameter('tag_id', openapi.IN_QUERY, description="test manual param",
                              type=openapi.TYPE_STRING)
        ],
    )
    def get(self, request, *args, **kwargs):
        key = request.GET.get('tag_id', False)
        if key:
            keys = key.split(',')
            self.queryset = NewsModel.objects.filter(hashtag_id__id=keys)
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

class NotificationView(APIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    @swagger_auto_schema(
        operation_id='notification',
        operation_description="post notifications",
        request_body=NotificationSerializer(),
        responses={
            '200': NotificationSerializer()
        },)

    def post(self, request, *args, **kwargs):
        title = request.data.get("title")
        title = request.data.get("title")
        title = request.data.get("title")
        title = request.data.get("title")

        return self.list(request, *args, **kwargs)
#         manual_parameters=[
#             openapi.Parameter('limit', openapi.IN_QUERY, description="Number of results to return per page.",
#                               type=openapi.TYPE_NUMBER)
#         ],
#     )