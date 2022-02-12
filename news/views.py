from django.shortcuts import render
from rest_framework.views import APIView

from config.responses import ResponseSuccess, ResponseFail
from .serializers import NewsModelSerializer
from .models import NewsModel


class NewsView(APIView):

    def get(self, request):
        news = NewsModel.objects.all()
        serializers = NewsModelSerializer(news, many=True)
        return ResponseSuccess(data=serializers.data, request=request.method)


