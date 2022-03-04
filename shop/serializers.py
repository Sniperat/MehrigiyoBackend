from rest_framework import serializers
from .models import PicturesMedicine, TypeMedicine, Medicine


class PicturesMedicineSerializer(serializers.ModelSerializer):

    class Meta:
        model = PicturesMedicine
        fields = '__all__'


class TypeMedicineSerializer(serializers.ModelSerializer):

    class Meta:
        model = TypeMedicine
        fields = '__all__'


class MedicineSerializer(serializers.ModelSerializer):
    pictures = PicturesMedicineSerializer(many=True)

    class Meta:
        model = Medicine
        fields = '__all__'




