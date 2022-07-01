from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView

from config.responses import ResponseSuccess, ResponseFail
from .serializers import NewsModelSerializer
from .models import NewsModel


class NewsView(viewsets.ModelViewSet):
    queryset = NewsModel.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = NewsModelSerializer

    def get(self, request):

        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return ResponseSuccess(data=self.get_paginated_response(serializer.data), request=request.method)

