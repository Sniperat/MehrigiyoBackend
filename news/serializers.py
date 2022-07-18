from rest_framework.serializers import ModelSerializer, Serializer, CharField
from .models import NewsModel, TagsModel


class TagsSerializer(ModelSerializer):
    class Meta:
        model = TagsModel
        fields = ['tag_name']


class NewsModelSerializer(ModelSerializer):
    hashtag = TagsSerializer()

    class Meta:
        model = NewsModel
        fields = '__all__'


class TagsWithNewsSerializer(ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        n = NewsModel.objects.filter(hashtag__tag_name=representation['tag_name'])
        representation['news'] = NewsModelSerializer(n, many=True).data
        return representation

    class Meta:
        model = TagsModel
        fields = ['tag_name']


class InputSerializer(Serializer):
    tag = CharField(max_length=50)
