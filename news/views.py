from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView

from config.responses import ResponseSuccess, ResponseFail
from .serializers import NewsModelSerializer
from .models import NewsModel
from .filters import NewsFilter


class NewsView(viewsets.ModelViewSet):
    queryset = NewsModel.objects.all()
    # permission_classes = (IsAuthenticated,)
    serializer_class = NewsModelSerializer
    filterset_class = NewsFilter

    def get(self, request):
        filtered_qs = self.filterset_class(request.GET, queryset=self.get_queryset()).qs

        page = self.paginate_queryset(filtered_qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return ResponseSuccess(data=self.get_paginated_response(serializer.data), request=request.method)
