from rest_framework import serializers

from comment.models import CommentDoctor, CommentMedicine


class CommentDoctorSerializer(serializers.ModelSerializer):
    medicine = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField()

    class Meta:
        model = CommentDoctor
        fields = '__all__'


class CommentMedicineSerializer(serializers.ModelSerializer):
    medicine = serializers.ReadOnlyField()
    user = serializers.ReadOnlyField()

    class Meta:
        model = CommentMedicine
        fields = '__all__'
