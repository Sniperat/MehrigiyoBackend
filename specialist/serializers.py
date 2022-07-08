from django.db.models import Sum
from rest_framework import serializers

from account.models import UserModel
from .models import Doctor, TypeDoctor, RateDoctor, Advertising
from comment.models import CommentDoctor

class AdvertisingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertising
        fields = '__all__'


class TypeDoctorSerializer(serializers.ModelSerializer):
    # get_doctors_count = serializers.SerializerMethodField('')
    class Meta:
        model = TypeDoctor
        fields = ['id', 'name', 'image', 'get_doctors_count']


class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField()
    type_doctor = TypeDoctorSerializer()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user = self.context['user']
        try:
            if instance in user.favorite_medicine.all():

                representation['is_favorite'] = True
            else:
                representation['is_favorite'] = False
        except:
            pass
        # doctors = CommentDoctor.objects.filter(doctor=representation,)
        # representation['rate'] = sum(instance.comments_doc.values('rate', flat=True))
        representation['rate'] = instance.total_rate or 0
        # representation['rate'] = Sum(instance__comments_doc__rate)
        return representation

    class Meta:
        model = Doctor
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = RateDoctor
        fields = '__all__'

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.client = self.context['request'].user
        instance.save()
        return instance




