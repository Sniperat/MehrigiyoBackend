from rest_framework import serializers
from .models import Doctor, TypeDoctor, RateDoctor, Advertising


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




