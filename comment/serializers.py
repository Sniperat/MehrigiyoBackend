from rest_framework import serializers

from comment.models import CommentDoctor, CommentMedicine


class CommentDoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentDoctor
        fields = '__all__'
        extra_kwargs = {
            'user': {'required': False},
            'doctor': {'required': False},
        }


class CommentMedicineSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentMedicine
        fields = '__all__'
        extra_kwargs = {
            'user': {'required': False},
            'medicine': {'required': False},
        }
