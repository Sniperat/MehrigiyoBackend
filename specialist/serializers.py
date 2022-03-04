from rest_framework import serializers
from .models import Doctor, TypeDoctor


class TypeDoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeDoctor
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField()

    class Meta:
        model = Doctor
        fields = '__all__'





