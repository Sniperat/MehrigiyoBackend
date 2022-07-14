from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics
from rest_framework.views import APIView

from config.responses import ResponseSuccess, ResponseFail
from .serializers import NewsModelSerializer
from .models import NewsModel
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
    )
    def get(self, request, *args, **kwargs):

        return self.list(request, *args, **kwargs)
    # def get(self, request):
    #     filtered_qs = self.filterset_class(request.GET, queryset=self.get_queryset()).qs
    #
    #     page = self.paginate_queryset(filtered_qs)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return ResponseSuccess(data=self.get_paginated_response(serializer.data), request=request.method)
