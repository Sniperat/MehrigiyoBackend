from rest_framework.serializers import ModelSerializer
from .models import NewsModel


class NewsModelSerializer(ModelSerializer):

    class Meta:
        model = NewsModel
        fields = '__all__'
